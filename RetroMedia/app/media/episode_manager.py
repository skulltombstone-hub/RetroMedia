from pathlib import Path

class EpisodeManager:

    def __init__(self):

        self.current = 0

        self.episodes = []

    def load(self, path):

        self.episodes = sorted([
            p for p in Path(path).iterdir()
            if p.suffix.lower() in [
                ".mp4",
                ".mkv"
            ]
        ])

    def next(self):

        if self.current < len(self.episodes)-1:
            self.current += 1

        return self.episodes[self.current]

    def previous(self):

        if self.current > 0:
            self.current -= 1

        return self.episodes[self.current]
