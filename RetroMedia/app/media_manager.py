import json
import shutil
from pathlib import Path

MEDIA_DIR = Path("media")

def create_media_entry(
    title,
    category,
    media_files,
    keybind,
    keyboard_id
):
    media_path = MEDIA_DIR / category / title

    media_path.mkdir(parents=True, exist_ok=True)

    for file in media_files:
        shutil.copy(file, media_path)

    metadata = {
        "title": title,
        "category": category,
        "keybind": keybind,
        "keyboard_id": keyboard_id,
        "delay_before_intro": 2,
        "delay_before_play": 3,
        "intro": "intro.mp4"
    }

    with open(media_path / "metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
