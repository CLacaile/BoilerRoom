from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Room

# home page
def index(request):
    room_list = get_list_or_404(Room)
    context = {
            'room_list': room_list,
    }
    return render(request, 'Boilr/index.html', context)

# room details
def detail(request, room_id):
   # try:
   #     room = Room.objects.get(id=room_id)
   # except Room.DoesNotExist:
   #     raise Http404("Room does not exist")
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'Boilr/detail.html', {'room': room})

# room stats
def stats(request, room_id):
    return HttpResponse("You're looking at the stats of room %s" % room_id)

