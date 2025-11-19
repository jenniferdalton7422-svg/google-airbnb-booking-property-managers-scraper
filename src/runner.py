import json
import logging
from pathlib import Path

from platforms.google_parser import GoogleParser
from platforms.airbnb_parser import AirbnbParser
from platforms.booking_parser import BookingParser
from pipelines.normalize_data import normalize_record
from pipelines.export_spreadsheet import export_to_json

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
INPUT_FILE = DATA_DIR / "input_queries.txt"
OUTPUT_FILE = DATA_DIR / "sample_output.json"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_queries():
 if not INPUT_FILE.exists():
 logging.error(f"Missing input file: {INPUT_FILE}")
 return []
 with open(INPUT_FILE, "r", encoding="utf-8") as f:
 return [line.strip() for line in f if line.strip()]

def run():
 queries = load_queries()
 if not queries:
 logging.warning("No queries loaded. Exiting.")
 return

 google = GoogleParser()
 airbnb = AirbnbParser()
 booking = BookingParser()

 all_results = []

 for q in queries:
 logging.info(f"Processing query: {q}")

 for parser in (google, airbnb, booking):
 try:
 raw_results = parser.search(q)
 for r in raw_results:
 normalized = normalize_record(r)
 all_results.append(normalized)
 except Exception as e:
 logging.error(f"Error in parser {parser.__class__.__name__}: {e}")

 export_to_json(all_results, OUTPUT_FILE)
 logging.info(f"Export completed → {OUTPUT_FILE}")

if __name__ == "__main__":
 run()