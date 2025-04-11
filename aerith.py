import typer
from typing_extensions import Annotated
from utils.logging import AerithLogger

logger = AerithLogger(timestamp=False)

def main(
        command: Annotated[str, typer.Argument(help="Arg: start, hello")],
):
    if command == "start":
        logger.log("Starting Application")
        from core.ui import BootScreen
        BootScreen().run()

    elif command == "exit":
        logger.log("Goodbye...")
    else:
        logger.warn("syntax error. only use lower case")

if __name__ == "__main__":
    typer.run(main)