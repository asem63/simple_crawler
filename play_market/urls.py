from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from play_market.views import CategoryViewSet, AppViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'app', AppViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
