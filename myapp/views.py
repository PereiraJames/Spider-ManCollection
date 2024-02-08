from django.shortcuts import render, HttpResponse
from .models import Amazingspiderman

# Create your views here.
def home(request):
    return render(request, "home.html")

def comic_list(request):
    items = Amazingspiderman.objects.all()

    items = items.order_by('series_year', 'issuenumber')

    return render(request, "comiclist.html", {"spidermancomics": items})