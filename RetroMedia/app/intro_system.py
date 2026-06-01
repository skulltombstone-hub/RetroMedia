import time

from player import RetroPlayer

player = RetroPlayer()

def play_intro_then_media(
    intro_path,
    media_path,
    delay_before_intro=2,
    delay_before_play=3
):

    time.sleep(delay_before_intro)

    if intro_path.exists():

        player.play_video(str(intro_path))

        while player.player.is_playing():
            time.sleep(0.1)

    time.sleep(delay_before_play)

    player.play_video(str(media_path))
