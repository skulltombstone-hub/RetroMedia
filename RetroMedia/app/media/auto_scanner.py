from pathlib import Path

def auto_detect_media():

    media_root = Path("media")

    detected = []

    for category in media_root.iterdir():

        for media in category.iterdir():

            detected.append(media)

    return detected
