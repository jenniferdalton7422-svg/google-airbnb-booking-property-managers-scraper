def normalize_record(record: dict) -> dict:
 """Convert raw scraper output into a clean normalized dictionary."""
 return {
 "name": record.get("name", "").strip(),
 "phone": record.get("phone", "").strip(),
 "email": record.get("email", "").strip(),
 "company": record.get("company", "").strip(),
 "properties_managed": int(record.get("properties_managed", 0)),
 "platform": record.get("platform", "").strip(),
 "source_url": record.get("source_url", "").strip()
 }