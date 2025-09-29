from fastapi import APIRouter, status


router = APIRouter()

@router.get("", status_code=status.HTTP_200_OK)
def get_health():
    """
    Router to get health to see if app is up
    """
    return {"message": "App is up & running !"}