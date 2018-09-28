import urllib3
from bs4 import BeautifulSoup


class GooglePlayCrawler:
    """
    Performs crawling in game categories section of google play market
    """
    def __init__(self, hl='en', gl='us'):
        """
        Basic initialization of class that accepts two parameters.
        :param hl: language code, defaults to 'en'
        :param gl: geolocation code, defaults to 'us'
        """
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
        """
        Helper method which builds url that is used during crawling.
        :param url: url to be used for building
        :return str: string with parameters attached if form of query_params
        """
        return self.base_url + url + '?' + '&'.join([
            '{}={}'.format(k, v) for k, v in self.params.items()
        ])

    def get_app_info_dict(self, raw_app: BeautifulSoup) -> dict:
        """
        Gets playmarket app info from given BeautifulSoup input.
        :param raw_app: BeautifulSoup object with all app information
        :return dict: dict that contains all information extracted from raw_app
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

    def getGameSubcategories(self) -> [dict, dict, ...]:
        """
        Retrieves game categories from play market
        :return list: list that contains dicts {href:str, title:str}
        """
        request = self.http.request('GET', self._build_url(self.base_game_url))
        soup = BeautifulSoup(request.data)
        games_subcategory_links = soup.select('a.leaf-submenu-link')
        return [
            {'href': link.attrs['href'], 'title': link.attrs['title']}
            for link in games_subcategory_links
        ]

    def getSubcategoryGames(self, subcategory_url: str) -> [dict, dict, ...]:
        """
        Retrieves games from specified category
        :param subcategory_url: url of subcategory to wirk with
        :return list: list that contains dicts filled with app information
        """
        request = self.http.request('GET', self._build_url(subcategory_url))
        soup = BeautifulSoup(request.data)
        subcategory_games = soup.select('div[data-uitype=500]')
        return [
            self.get_app_info_dict(game)
            for game in subcategory_games
        ]
