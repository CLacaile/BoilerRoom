from django.urls import path
from . import views

app_name = 'Boilr'
urlpatterns = [
        # ex : /boilr/
	path('', views.index, name='index'),
        # ex : boilr/room/1
        path('room/<int:room_id>/', views.detail, name='detail'),
        # ex : boilr/room/1/stats
        path('room/<int:room_id>/stats', views.stats, name='stats'),

]
