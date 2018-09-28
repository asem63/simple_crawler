from django.conf.urls import url, include

urlpatterns = [
    url(
        r'^play_market/', include('play_market.urls')
    ),
]
