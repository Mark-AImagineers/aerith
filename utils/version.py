import json
from pathlib import Path

class VersionManager:
    def __init__(self, path=None):
        if path is None:
            path = Path.cwd() / "version.json"
        self._path = path
        self._data = self._load()

    def _load(self):
        if not self._path.exists():
            raise FileNotFoundError("version.json is missing")
        with open(self._path, "r") as f:
            return json.load(f)

    @property
    def version(self):
        return self._data.get("version")

    @property
    def build(self):
        return self._data.get("build")

    @property
    def commit(self):
        return self._data.get("commit")

    @property
    def environment(self):
        return self._data.get("environment")

    @property
    def service(self):
        return self._data.get("service")

    def raw(self):
        return self._data