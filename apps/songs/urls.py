from django.urls import path

from . import views


urlpatterns = [
    path('',  views.SongListView, name='song_list')
]