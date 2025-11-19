def safe_extract(value):
 """Basic validation wrapper."""
 if not value:
 return ""
 return str(value)