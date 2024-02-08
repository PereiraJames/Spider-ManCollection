from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Amazingspiderman

# Create your views here.
def home(request):
    return render(request, "home.html")

def comic_list(request,details= None):
    items = Amazingspiderman.objects.all()
    items = items.order_by('series_year', 'issuenumber')

    if request.method == 'POST':
        comic_id = request.POST.get('comic_id')
        new_state = request.POST.get('new_state')
        
        print("Comic ID:", comic_id)
        print("New State:", new_state)

        Amazingspiderman.objects.filter(comicid=comic_id).update(state=new_state)

    return render(request, "comiclist.html", {"spidermancomics": items})


def insert_data(request):
    if request.method == 'POST' and request.is_ajax():
        # Extract data from the request
        data = request.POST.get('your_data')

        # Perform database insertion
        try:
            Amazingspiderman.objects.create(your_field=data)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})