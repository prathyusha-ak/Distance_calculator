# Distance Calculator

A web application to calculate the distance between two addresses.

## Prerequisites
- Docker and Docker Compose installed

## How to Run

1. **Clone the repository**
   Run the commands below in the terminal:
   git clone https://github.com/yourusername/distance-calculator.git
   cd distance-calculator
   

2. **Start the application**
   Run the command below in the terminal:
   docker-compose up --build
   

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - DB Connection string: mongodb://localhost:27017

## Project Structure
- `backend/` - FastAPI backend
- `frontend/` - SvelteKit frontend
- `docker-compose.yml` - Orchestrates all services

## Stopping the Application
Run the command below in the terminal:
docker-compose down


## Notes
- MongoDB runs as a container by default. For production, we can use MongoDB Atlas and update the connection string in `backend/src/db/q.py`.
- If you change backend or frontend code, re-run `docker-compose up --build`.

