import json
from pathlib import Path

MEDIA_ROOT = Path("media")

media_registry = {}

def scan_media():

    media_registry.clear()

    for category in MEDIA_ROOT.iterdir():

        if not category.is_dir():
            continue

        for media_folder in category.iterdir():

            metadata_file = media_folder / "metadata.json"

            if not metadata_file.exists():
                continue

            with open(metadata_file, "r", encoding="utf-8") as f:
                metadata = json.load(f)

            key = (
                metadata["keyboard_id"],
                metadata["keybind"]
            )

            media_registry[key] = {
                "path": media_folder,
                "metadata": metadata
            }

def get_media(keyboard_id, keybind):

    return media_registry.get(
        (keyboard_id, keybind)
    )
