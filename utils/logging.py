import datetime
from utils.version import VersionManager

version_manager = VersionManager()

class AerithLogger:
    def __init__(
        self,
        service_name=f"[Aerith][v.{version_manager.version}]",
        enable=True,
        timestamp=True,
    ):
        self.service_name = service_name
        self.enable = enable
        self.show_timestamp = timestamp

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _prefix(self):
        if self.show_timestamp:
            return f"[{self._timestamp()}] [{self.service_name}]"
        else:
            return f"[{self.service_name}]"

    def log(self, message):
        if self.enable:
            print(f"{self._prefix()} {message}")

    def warn(self, message):
        if self.enable:
            print(f"{self._prefix()}[! WARNING] {message}")

    def error(self, message):
        if self.enable:
            print(f"{self._prefix()}[!! ERROR] {message}")
