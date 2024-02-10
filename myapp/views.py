from django.shortcuts import render
from .models import Amazingspiderman
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def home(request):
    items = Amazingspiderman.objects.all()
    items = items.order_by('series_year', 'issuenumber')

    return render(request, "home.html", {"spidermancomics": items})

def create(request):
    if request.method == 'POST':
        print("test")
        print(request.POST)
        print("Comic ID:", request.POST['csrfmiddlewaretoken'])
        changed_state = request.POST['changed_state']
        comic_id = request.POST['comic_id']
        
        
        print("Comic ID:", comic_id)
        print("New State:", changed_state)

        Amazingspiderman.objects.filter(comicid=comic_id).update(state=changed_state)
        success = "Updated " + changed_state + " for " + comic_id

        return HttpResponse(success)
