"""
URL configuration for home app
"""
from django.conf.urls import url

from home.views import HomeView, ContactView, AboutView, ResumeView

app_name = 'home'
urlpatterns = [
    url(r'^resume/', ResumeView.as_view(), name='resume'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^contact/', ContactView.as_view(), name='contact'),
    url(r'^$', HomeView.as_view(), name="home"),
]
