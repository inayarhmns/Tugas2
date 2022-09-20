# TODO: Implement Routings Here
from django.urls import path
from . import views

app_name = 'mywatchlist'

urlpatterns = [
     path('', views.show_mywatchlist_html, name='show_mywatchlist_html'),
    path('html/', views.show_mywatchlist_html, name='show_mywatchlist_html'),
    path('json/', views.show_watchlist_json, name='show_watchlist_json'),
    path('xml/', views.show_watchlist_xml, name='show_watchlist_xml'),


]