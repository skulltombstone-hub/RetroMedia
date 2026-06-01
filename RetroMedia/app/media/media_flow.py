import time

from app.players.mpv_player import MPVPlayer

player = MPVPlayer()

def cinematic_delay(seconds):

    time.sleep(seconds)

def start_media_flow(media):

    intro_delay = media[9]

    start_delay = media[10]

    intro = media[6]

    content = media[5]

    cinematic_delay(intro_delay)

    if intro:

        player.play(intro)

        while player.player.core_idle == False:
            time.sleep(0.1)

    cinematic_delay(start_delay)

    player.play(content)
