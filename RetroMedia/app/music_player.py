import vlc

class MusicPlayer:

    def __init__(self):

        self.instance = vlc.Instance()

        self.player = self.instance.media_player_new()

    def play(self, path):

        media = self.instance.media_new(path)

        self.player.set_media(media)

        self.player.play()

    def stop(self):

        self.player.stop()
