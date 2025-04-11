import random
import importlib
from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Container
from utils.version import VersionManager
from commands import core

ver = VersionManager()
COMMANDS = {
    **core.CMDS,
}

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
            f"[green]Aerith v{ver.version} online. ",
            "[green]Stable... ",
            "",
            "[bold green]Aerith: Welcome back, Mark.",
            "[green]Aerith: What are we doing today?"
        ]
        self.current_line = 0
        self.current_char = 0
        self.display_text = ""
        self._schedule_next_step()

    def _schedule_next_step(self):
        delay = random.uniform(0.01, 0.03)
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
                input_box = Input(placeholder="", id="input")
                response_box = Static("", id="response")

                self.mount(input_box)
                self.mount(response_box)

                self.set_focus(input_box)
                pass
    
    #----------------------------------#
    # Commands                         #
    #----------------------------------#
    def on_input_submitted(self, event: Input.Submitted) -> None:
        key = event.value.strip().lower()
        msg_box = self.query_one("#boot-msg", Static)
        output = ""

        try:
            if key in COMMANDS:
                result = COMMANDS[key]()

                if result == "__clear__":
                    msg_box.update("")
                    event.input.value = ""
                    return
                else:
                    output = f"[green]Aerith: {result}"
            else:
                output = f"[green]Aerith: Unknown command '{key}'"

        except AttributeError:
            output = f"[green]Aerith: Command '{key}' found, but is not callable."

        except Exception as e:
            output = f"[red]Aerith: Error while executing '{key}': {str(e)}"

        msg_box.update(msg_box.renderable + f"\n{output}")
        event.input.value = ""