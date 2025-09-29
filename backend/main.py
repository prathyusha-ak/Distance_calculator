from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from src.services.limiter import limiter

from src.db.q import MongoDBConnection
from src.routers import distance, health
from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start db connection
    MongoDBConnection.connect()
    yield
    # Shutdown
    if MongoDBConnection.client:
        MongoDBConnection.client.close()
        print("MongoDB connection closed")


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Distance Calculator API"}

def rate_limit_msg(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Too many retries"}
    )

# Attach limiter + exception handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_msg)
app.add_middleware(SlowAPIMiddleware)


# Configure CORS
origins = [
    "http://localhost:5173",  # Svelte app
    # "https://prod_URL"  # add production frontend URL if needed in future
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],    # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],    # allow all headers
)

app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    distance.router,
    prefix="/api/v1",
    tags=["Distance"]
)




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
