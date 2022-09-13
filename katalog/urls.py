# TODO: Implement Routings Here
from django.urls import path, include
from katalog.views import index

app_name = 'katalog'

urlpatterns = [
    path('', index, name='show_katalog'),
]