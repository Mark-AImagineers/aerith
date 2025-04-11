import datetime
from utils.version import VersionManager

version_manager = VersionManager()

class AerithLogger:
    def __init__(self, service_name=f"[Aerith][v.{version_manager.version}]", enable=True):
        self.service_name = service_name
        self.enable = enable

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log(self, message):
        if self.enable:
            print(f"[{self._timestamp()}] [{self.service_name}] {message}")

    def warn(self, message):
        if self.enable:
            print(f"[{self._timestamp()}] [{self.service_name}][! WARNING] {message}")

    def error(self, message):
        if self.enable:
            print(f"[{self._timestamp()}] [{self.service_name}][!! ERROR] {message}")
