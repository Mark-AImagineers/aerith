import json
import asyncio
import sys
import os
import subprocess
from pathlib import Path
from utils.terminal import TerminalManager

ter = TerminalManager()

async def update_version(say, new_version="0.0.1"):
    await say("Loading version.json...")

    path = Path(__file__).resolve().parent.parent / "version.json"

    try:
        with open(path, "r") as f:
            data = json.load(f)
    except Exception as e:
        say(f"Error reading version.json: {str(e)}")
        return "Aborted."

    await say(f"Current version is: {data.get('version')}")
    await say(f"Updating version to {new_version}...")

    data["version"] = new_version

    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        await say(f"Error writing version.json: {str(e)}")
        return "Failed."

    await say(f"Version updated to {new_version}")
    return ter.get_voiceline("command")

async def restart(say):
    await say("Ok. Restarting System")

    python = sys.executable
    root = os.path.dirname(os.path.dirname(__file__))
    main_script = os.path.join(root, "aerith.py")

    subprocess.Popen([python, main_script, "start"])
    sys.exit(0)

def cls():
    return "__clear__"

CMDS = {
    "cls": cls,
    "clear": cls,
    "update version": update_version,
    "update_version": update_version,
    "reset": restart,
    "restart": restart
}