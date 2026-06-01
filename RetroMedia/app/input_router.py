from media_registry import get_media
from intro_system import play_intro_then_media

def handle_input(
    keyboard_id,
    keybind
):

    media = get_media(
        keyboard_id,
        keybind
    )

    if not media:
        return

    metadata = media["metadata"]

    media_path = media["path"]

    intro = media_path / metadata["intro"]

    video_files = list(media_path.glob("*.mp4"))

    if not video_files:
        return

    play_intro_then_media(
        intro_path=intro,
        media_path=video_files[0],
        delay_before_intro=metadata.get(
            "delay_before_intro", 2
        ),
        delay_before_play=metadata.get(
            "delay_before_play", 3
        )
    )
