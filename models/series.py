class Series:

    def __init__(self, link):
        self.title = None
        self.link = link
        self.path = None
        self.episodes = []

    def __str__(self):
        return self.title

    def set_series_title(self, title):
        self.title = title

    def set_series_path(self, path):
        self.path = path

    def get_series_title(self):
        return self.title

    def get_series_link(self):
        return self.link

    def add_episode(self, episode):
        self.episodes.append(episode)

    def get_series_episodes(self):
        return self.episodes

    def get_series_path(self):
        return self.path


class Episode:

    def __init__(self, episode_number, episode_link):
        self.episode_number = episode_number
        self.episode_link = episode_link
        self.quality = None

    def get_episode_number(self):
        return self.episode_number

    def get_episode_link(self):
        return self.episode_link

    def set_quality(self, quality):
        self.quality = quality
