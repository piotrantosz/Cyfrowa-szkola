from django.conf.urls import url

from .views import (
    news_list,
    news_detail,
)


urlpatterns = [
    url(r'^', news_list, name="list"),
    url(r'^(?P<id>\d+)/$', news_detail, name='detail'),
]