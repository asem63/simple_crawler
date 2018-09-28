from django.core.management.base import BaseCommand

from play_market.crawler import GooglePlayCrawler
from play_market.models import Category, App


class Command(BaseCommand):
    help = (
        'Command that runs google play scrapper and fills database with'
        'results'
    )

    def handle(self, *args, **options):
        gcr = GooglePlayCrawler()
        # get game categories
        game_categ_arr = gcr.getGameSubcategories()

        for game_categ_dict in game_categ_arr:
            # write game category to db if not exist
            title = game_categ_dict.get('title')
            href = game_categ_dict.get('href')
            mnemonic_name = href.split('/')[-1]
            category, _ = Category.objects.get_or_create(
                mnemonic_name=mnemonic_name, title=title
            )
            # get games in specific category
            games = gcr.getSubcategoryGames(href)
            for game in games:
                # write game to db if not exist
                App.objects.get_or_create(
                    category=category,
                    app_id=game.get('id'),
                    title=game.get('title'),
                    image=game.get('image'),
                    description=game.get('description'),
                    url=game.get('url'),
                    dev_id=game.get('dev_id'),
                    dev=game.get('dev'),
                    score=game.get('score')
                )
