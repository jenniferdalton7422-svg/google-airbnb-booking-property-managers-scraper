import logging
from .helpers_validation import safe_extract

class AirbnbParser:
 def search(self, query: str):
 logging.info(f"AirbnbParser: searching '{query}'")
 return [
 {
 "name": "CityHost Rentals",
 "phone": "+1 555-111-9999",
 "email": "contact@cityhost.com",
 "company": "CityHost Rentals",
 "properties_managed": 45,
 "platform": "Airbnb",
 "source_url": safe_extract("https://airbnb.com/example")
 }
 ]