from .api import fetch_repos
from .repo import Repository


class CLI():
    def __init__(self):
        self._user_input = ""

    def start(self):
        name = input('Enter account name: ')
        fetch_repos(name)
        self.menu()

    def menu(self):
        for inx, repo in enumerate(Repository.all, start=1):
            print(f'{inx}. {repo.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input('Select repo number for more info')
            if not self.valid_input(self._user_input):
                return ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print('Sorry,that is not a valid input')
            self.menu()

    def show_repo(self):
        repo = Repository.find_by_input(self._user_input)
        print(repo.name)
        print(f'Number of forks {repo.forks}')
        print(f'url: {repo.url}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repository.all)
