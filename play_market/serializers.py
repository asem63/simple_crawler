from rest_framework.serializers import ModelSerializer
from play_market.models import Category, App


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('mnemonic_name', 'title')


class AppSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = App
        fields = (
            'category', 'app_id', 'title', 'image', 'description', 'url',
            'dev', 'dev_id', 'score'
        )
