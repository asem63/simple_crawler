import urllib3
from bs4 import BeautifulSoup


class GooglePlayCrawler:
    def __init__(self, hl='en', gl='us'):
        self.language = hl
        self.geolocation = gl
        self.base_url = "https://play.google.com"
        self.base_game_url = "/store/apps/category/GAME"
        self.http = urllib3.PoolManager()
        self.params = {
            'hl': self.language,
            'gl': self.geolocation
        }

    def _build_url(self, url=''):
        return self.base_url + url + '?' + '&'.join([
            '{}={}'.format(k, v) for k, v in self.params.items()
        ])

    def get_app_info_dict(self, raw_app: BeautifulSoup) -> dict:
        """
        Pickle playmarket app info from given BeautifulSoup input.
        """

        url = (
            self.base_url
            + raw_app.select_one('a.card-click-target').attrs['href']
        )
        dev_raw_app = raw_app.select_one('a.subtitle')
        dev_id = dev_raw_app.attrs['href'].split('=')[1]
        dev = dev_raw_app.attrs['title']
        score = raw_app.select_one('div.tiny-star')
        if score:
            score = score.attrs['aria-label'].strip().split(' ')[1]

        return {
            'id': raw_app.attrs['data-docid'],
            'title': raw_app.select_one('a.title').attrs['title'],
            'image': (
                raw_app.select_one('img.cover-image')
                .attrs['src'].split('=')[0]
            ),
            'description': raw_app.select_one('div.description').text.strip(),
            'url': url,
            'dev_id': dev_id,
            'dev': dev,
            'score': score,
        }

    def getGameSubcategories(self):
        request = self.http.request('GET', self._build_url(self.base_game_url))
        soup = BeautifulSoup(request.data)
        games_subcategory_links = soup.select('a.leaf-submenu-link')
        return [
            {'href': link.attrs['href'], 'title': link.attrs['title']}
            for link in games_subcategory_links
        ]

    def getSubcategoryGames(self, subcategory_url):
        request = self.http.request('GET', self._build_url(subcategory_url))
        soup = BeautifulSoup(request.data)
        subcategory_games = soup.select('div[data-uitype=500]')
        return [
            self.get_app_info_dict(game)
            for game in subcategory_games
        ]
