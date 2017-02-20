from django.conf.urls import url

from .views import (
    news_list,
    news_detail,
    news_create,
    news_update,
    news_delete,
)

urlpatterns = [
    url(r'^$', news_list, name="list"),
    url(r'^create/', news_create, name="create"),
    url(r'^(?P<id>\d+)/$', news_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', news_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', news_delete),
]
