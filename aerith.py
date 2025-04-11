import typer

app = typer.Typer()

@app.command()
def start():
    from utils.logging import AerithLogger
    from utils.version import VersionManager

    log = AerithLogger()
    version = VersionManager()

    log.log("Boot sequence started...")
    log.log(f"Running in {version.environment} mode.")

if __name__ == "__main__":
    app()
