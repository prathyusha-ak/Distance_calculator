from typing import List
from pydantic import BaseModel

class GeoCodes(BaseModel):
    place_id: int
    licence: str
    osm_type: str
    osm_id: int
    lat: str
    lon: str
    category: str
    type: str
    place_rank: int
    importance: float
    addresstype: str
    name: str
    display_name: str
    boundingbox: List[str]