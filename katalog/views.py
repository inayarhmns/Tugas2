from django.shortcuts import render

# TODO: Create your views here.
def index(request):
    return render(request, 'katalog.html')