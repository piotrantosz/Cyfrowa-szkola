"""portfolios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', include('userprofile.urls')),
    url(r'^guide/$', TemplateView.as_view(template_name="guide.html"), name='guide'),
    url(r'^about-project/$', TemplateView.as_view(template_name="about_project.html"), name='about-project'),
    url(r'^download/$', TemplateView.as_view(template_name="download.html"), name='download'),
    url(r'^schedule/$', TemplateView.as_view(template_name="schedule.html"), name='schedule'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
