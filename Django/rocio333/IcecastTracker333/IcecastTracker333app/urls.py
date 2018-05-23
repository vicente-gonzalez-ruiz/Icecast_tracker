from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.channel_list),
	url(r'^play', views.play_channel),
	url(r'^hello', views.hello),
]