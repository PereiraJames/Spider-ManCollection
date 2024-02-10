from django.shortcuts import render, HttpResponse
from .models import Amazingspiderman
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def comic_list(request):
    items = Amazingspiderman.objects.all()
    items = items.order_by('series_year', 'issuenumber')

    if request.method == 'POST':
        comic_id = request.POST.get('comic_id')
        new_state = request.POST.get('new_state')
        
        print("Comic ID:", comic_id)
        print("New State:", new_state)

        scroll_position = request.session.pop('scroll_position', None)

        Amazingspiderman.objects.filter(comicid=comic_id).update(state=new_state)

    return render(request, "comiclist.html", {"spidermancomics": items})
    
def collections(request):
    items = Amazingspiderman.objects.all()
    items = items.order_by('series_year', 'issuenumber')

    if request.method == 'POST':
        comic_id = request.POST.get('comic_id')
        new_state = request.POST.get('new_state')
        
        print("Comic ID:", comic_id)
        print("New State:", new_state)

        scroll_position = request.session.pop('scroll_position', None)

        Amazingspiderman.objects.filter(comicid=comic_id).update(state=new_state)
        return HttpResponse("Hello!")

    return render(request, "collections.html", {"spidermancomics": items})

def update_record(request, record_id):
    items = Amazingspiderman.objects.all()
    items = items.order_by('series_year', 'issuenumber')

    if request.method == 'POST':
        comic_id = request.POST.get('comic_id')
        new_state = request.POST.get('new_state')
        Amazingspiderman.objects.filter(comicid=comic_id).update(state=new_state)

        Amazingspiderman.save()
        return JsonResponse({'success': True})
    else:
        my_model_instance = Amazingspiderman.objects.get(pk=record_id)
        return render(request, 'update_form.html', {'instance': my_model_instance})