import random
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container
from utils.version import VersionManager

ver = VersionManager()

class BootScreen(App):
    CSS_PATH = None

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Aerith boot sequence initializing...\n", id="boot-msg"),
            id="boot-container"
        )

    def on_mount(self) -> None:
        self.steps = [
            "[green]Initializing Aerith Core...",
            "[green]Mounting encrypted archives. ",
            f"[green]Checking Version Tag: v{ver.version}",
            f"[green]Utilizing Build Signature: {ver.build}",
            f"[green]Validating System Environment",
            f"[green]Active runtime: {ver.environment}",
            "[green]Establishing link...",
            "[green]Sync Protocol Established ",
            "[green]All systems Online. ",
            "[green]Stable... ",
            "",
            "[bold green]Welcome back, Mark.",
            "[green]What are we doing today?"
        ]
        self.current_line = 0
        self.current_char = 0
        self.display_text = ""
        self._schedule_next_step()

    def _schedule_next_step(self):
        delay = random.uniform(0.01, 0.09)
        self.set_timer(delay, self._type)

    def _type(self):
        if self.current_line < len(self.steps):
            line = self.steps[self.current_line]
            if self.current_char < len(line):
                self.display_text += line[self.current_char]
                self.query_one("#boot-msg", Static).update(self.display_text)
                self.current_char += 1
                self._schedule_next_step()
            else:
                self.display_text += "\n"
                self.current_line += 1
                self.current_char = 0
                self._schedule_next_step()
        else:
            # Done typing, no need to schedule more
            pass