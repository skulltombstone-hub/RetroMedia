from app.media.media_registry import find_media
from app.players.media_flow import start_media_flow

def handle_input(
    keyboard_id,
    key
):

    media = find_media(
        keyboard_id,
        key
    )

    if not media:
        return

    start_media_flow(media)
