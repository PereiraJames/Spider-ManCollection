from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("comiclist/", views.comic_list, name="Comics List"),
    path("collections/", views.collections, name="Comics List"),
    path('update/<int:record_id>/', views.update_record, name='update-record'),

]

