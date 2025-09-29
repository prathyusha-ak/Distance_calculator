import requests


class NominatimService:
    base_url = "https://nominatim.openstreetmap.org/search"
    headers = {
        "User-Agent": "MyGeocoderApp/1.0 (myemail@example.com)"
        }
    
    def get_co_ordinates(self, address: str) -> tuple:
        params = {"q": address,  "format": "jsonv2", "limit": 1}
        response = requests.get(url=self.base_url, params=params, headers=self.headers)
        if response.status_code == 200:
            address_list = response.json()
            if not address_list:
                raise Exception(f"No geo codes found for given address: {address}")
            return address_list[0]
        else:
            # raise custom exception
            pass