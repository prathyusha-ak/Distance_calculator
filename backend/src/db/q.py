from motor.motor_asyncio import AsyncIOMotorClient

class MongoDBConnection:
    client = None
    
    @staticmethod
    def connect():
        if not MongoDBConnection.client:
            print("Connecting to MongoDB...")
            #MongoDBConnection.client = AsyncIOMotorClient("mongodb://localhost:27017")
            MongoDBConnection.client = AsyncIOMotorClient("mongodb://mongodb:27017")
            print("Connection successful...")
            
    @staticmethod
    def get_database(database_name: str):
        if not MongoDBConnection.client:
            raise ValueError("MongoDB client is not connected")
        
        return MongoDBConnection.client[database_name]