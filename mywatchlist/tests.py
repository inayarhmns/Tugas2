from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist_html, show_watchlist_json, show_watchlist_xml
# from .models import WatchlistItem
# Create your tests here.
client = Client()


class TestUrls(TestCase):
    def test(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code , 200)
    def test_html(self):
        response = self.client.get('/mywatchlist/html/', follow=True)
        self.assertEqual(response.status_code , 200)
    def test_json(self):
        response = self.client.get('/mywatchlist/json/', follow=True)
        self.assertEqual(response.status_code , 200)
    def test_xml(self):
        response = self.client.get('/mywatchlist/xml/', follow=True)
        self.assertEqual(response.status_code , 200)
