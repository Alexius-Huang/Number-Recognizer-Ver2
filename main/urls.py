from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^feed/$', views.feed, name = 'feed'),
  url(r'^generate_data/$', views.generate_data, name='generate_data')
]