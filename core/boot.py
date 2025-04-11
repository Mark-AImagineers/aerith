import json
from pathlib import Path

def load_version():
    version_path = Path(__file__).resolve().parent.parent / "version.json"
    with open(version_path, "r") as f:
        return json.load(f)
    
