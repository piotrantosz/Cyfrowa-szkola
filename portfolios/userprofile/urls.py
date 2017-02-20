from django.conf.urls import url

from .views import (
    profile_detail,
    profile_update
)

urlpatterns = [
    url(r'^$', profile_detail, name="account_profile"),
    url(r'^edit/', profile_update, name="account_edit"),
]
