from fastapi import APIRouter, HTTPException, Request, status
import logging
import re

from src.services.limiter import limiter
from src.models.geocodes_models import GeoCodes
from src.db.q import MongoDBConnection
from src.services.nominatim_service import NominatimService
from src.utils.distance_calculator import calculate_distance

router = APIRouter()

# Set up logger
logger = logging.getLogger("distance_api")
logging.basicConfig(level=logging.INFO)

def validate_address(address: str) -> bool:
    # Allows only letters, numbers, spaces, commas, periods, and hyphens
    pattern = r'^[\w\s,.-]+$'
    return bool(re.match(pattern, address))

@router.get("", status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def get_distance(request: Request, source: str, destination: str):
    """
    Gets distance between source & destination in kms & miles
    """
    # Input validation
    if not validate_address(source) or not validate_address(destination):
        logger.warning(f"Invalid address input: source='{source}', destination='{destination}'")
        raise HTTPException(status_code=400, detail="Invalid address format.")

    try:
        logger.info(f"Calculating distance: source='{source}', destination='{destination}'")
        nominatim_service = NominatimService()
        source_co_ordinates_data = nominatim_service.get_co_ordinates(source)
        source_geo_code_object = GeoCodes(**source_co_ordinates_data)
        destination_co_ordinates_data = nominatim_service.get_co_ordinates(destination)
        destination_code_object = GeoCodes(**destination_co_ordinates_data)
        distance_in_km, distance_in_miles = calculate_distance(source_geo_code_object, destination_code_object)
        db_data = {
            "source": source, 
            "destination": destination, 
            "distanceKms": round(distance_in_km, 2), 
            "distanceMiles": round(distance_in_miles, 2), 
        }
        insert_result = await MongoDBConnection.get_database("mydatabase")["distance_queries"].insert_one(db_data)
        logger.info(f"Distance calculated and stored: {db_data}")
        return {
            "inserted_id": str(insert_result.inserted_id),
            "distanceKms": round(distance_in_km, 2), 
            "distanceMiles": round(distance_in_miles, 2), 
        }
    except Exception as ex:
        logger.error(f"Error calculating distance: {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
    
    
@router.get("/history", status_code=status.HTTP_200_OK)
async def get_historical_records():
    """
    Fetches historic data of distance queries from database
    """
    db_records_cursor = MongoDBConnection.get_database("mydatabase")["distance_queries"].find({}, {"_id": 0})
    db_records = await db_records_cursor.to_list()
    return db_records