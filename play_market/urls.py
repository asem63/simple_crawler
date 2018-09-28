from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from play_market.views import CategoryViewSet, AppViewSet, ForseCrawlView

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'app', AppViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/force_crawl', ForseCrawlView.as_view()),
]
