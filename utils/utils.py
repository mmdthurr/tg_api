import requests
from fake_useragent import UserAgent


class Req:
    _agent = UserAgent()

    @staticmethod
    def session():
        session = requests.Session()
        session.headers.update({
            "User-Agent": Req._agent.chrome
        })
        return session


class Url:
    def __init__(self, url: str = None):
        self.url = url

    def url_join(self, *args):
        self.url = self.url + ''.join(args)
        return self.url

    @property
    def scheme(self):
        return self.url.split('://')[0]

    @property
    def domain(self):
        return self.url.split('://')[1].split('/')[0]

    @property
    def path_array(self):
        return self.url.split('://')[1].split('/')[1:]

