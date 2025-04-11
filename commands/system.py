import json
from pathlib import Path
import asyncio


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

    return f"Version updated to {new_version}"

def cls():
    return "__clear__"

CMDS = {
    "cls": cls,
    "clear": cls,
    "update version": update_version,
    "update_version": update_version
}