from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import WatchlistItem

# Create your views here.
def show_mywatchlist_html(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
    'watch_list' : data_watchlist,
    'nama' : 'Inaya Rahmanisa',
    'npm'  : '2106708330',
    }
    return render(request, "mywatchlist.html", context)

def show_watchlist_json(request):       
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_watchlist_xml(request):       
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
