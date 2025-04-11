import random
import asyncio
from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Container
from utils.version import VersionManager
from utils.terminal import TerminalManager
from commands import system

ver = VersionManager()
ter = TerminalManager()

COMMANDS = {
    **system.CMDS,
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
            f"[bold green]Aerith: Mark, {ter.get_voiceline("greetings")}",
            f"[green]Aerith: {ter.get_voiceline("command")}"
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
    def say(self, message):
        msg_box = self.query_one("#boot-msg", Static)
        msg_box.update(msg_box.renderable + f"\n[green]Aerith: {message}")

    #----------------------------------#
    # Commands                         #
    #----------------------------------#
    async def on_input_submitted(self, event: Input.Submitted) -> None:
        msg_box = self.query_one("#boot-msg", Static)
        user_input = event.value.strip().lower()

        # Split input into words
        parts = user_input.split()
        key = " ".join(parts[:2]) if len(parts) >= 2 else parts[0]
        args = parts[2:] if len(parts) >= 2 else parts[1:]

        async def say(message: str):
            msg_box.update(msg_box.renderable + "\n")
            for char in message:
                msg_box.update(msg_box.renderable + char)
                await asyncio.sleep(0.02)

        try:
            if key in COMMANDS:
                result = await COMMANDS[key](say, *args)

                if result == "__clear__":
                    msg_box.update("")
                elif result:
                    await say(result)
            else:
                await say(f"Unknown command '{key}'")

        except AttributeError:
            await say(f"Command '{key}' found, but is not callable.")

        except Exception as e:
            await say(f"Error while executing '{key}': {str(e)}")

        event.input.value = ""
