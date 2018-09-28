from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from play_market.models import Category, App
from play_market.serializers import CategorySerializer, AppSerializer
from play_market.tasks import crawl_play_market


class ForseCrawlView(APIView):
    """
    View that invokes celery task which runs crawl_play_market command
    """

    def get(self, request):
        crawl_play_market.delay()
        return Response("Work in progress...")


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AppViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
