''' Defining the Repo class '''


class Repository():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._forks = data['forks']
        self._url = data['url']
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def forks(self):
        return self._forks

    @property
    def url(self):
        return self._url

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]
