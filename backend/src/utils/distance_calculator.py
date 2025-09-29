import math

from src.models.geocodes_models import GeoCodes

def calculate_distance(source: GeoCodes, destination: GeoCodes):
    """
    Calculates distance between two latitude-longitude coordinates.
    
    Parameters:
    coord1 : tuple of float (lat1, lon1)
    coord2 : tuple of float (lat2, lon2)
    
    Returns:
    (distance_km, distance_miles) : tuple of float
    """
    # Convert latitude and longitude from degrees to radians
    source_lat_rad = math.radians(float(source.lat))
    source_lon_rad = math.radians(float(source.lon))
    destination_lat_rad = math.radians(float(destination.lat))
    destination_lon_rad = math.radians(float(destination.lon))
    
    # Haversine formula
    dlat = destination_lat_rad - source_lat_rad
    dlon = destination_lon_rad - source_lon_rad
    a = math.sin(dlat / 2)**2 + math.cos(source_lat_rad) * math.cos(destination_lat_rad) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    R_km = 6371  # Radius of Earth in kilometers
    R_miles = 3956  # Radius of Earth in miles
    
    distance_km = R_km * c
    distance_miles = R_miles * c
    
    return distance_km, distance_miles
