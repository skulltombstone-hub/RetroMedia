import vlc
import time

class RetroPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play_video(self, path):
        media = self.instance.media_new(path)
        self.player.set_media(media)

        self.player.set_fullscreen(True)

        self.player.play()

    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()
