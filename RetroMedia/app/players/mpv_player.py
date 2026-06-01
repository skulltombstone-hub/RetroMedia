import mpv

class MPVPlayer:

    def __init__(self):

        self.player = mpv.MPV(
            fullscreen=True,
            osc=False,
            input_default_bindings=True,
            border=False
        )

    def play(self, file):

        self.player.play(file)

    def stop(self):

        self.player.stop()

    def pause(self):

        self.player.pause = not self.player.pause
