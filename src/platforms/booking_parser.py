import logging
from .helpers_validation import safe_extract

class BookingParser:
 def search(self, query: str):
 logging.info(f"BookingParser: searching '{query}'")
 return [
 {
 "name": "StayMasters Co.",
 "phone": "+1 555-222-3333",
 "email": "hello@staymasters.com",
 "company": "StayMasters",
 "properties_managed": 61,
 "platform": "Booking.com",
 "source_url": safe_extract("https://booking.com/example")
 }
 ]