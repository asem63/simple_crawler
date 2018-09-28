from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from play_market.models import Category, App
from play_market.serializers import CategorySerializer, AppSerializer


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AppViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
