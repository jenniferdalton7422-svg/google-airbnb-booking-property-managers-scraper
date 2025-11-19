import json
from pathlib import Path

def export_to_json(records, filepath: Path):
 filepath.parent.mkdir(parents=True, exist_ok=True)
 with open(filepath, "w", encoding="utf-8") as f:
 json.dump(records, f, indent=2)