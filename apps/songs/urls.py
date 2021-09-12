from django.urls import path

from . import views


urlpatterns = [
    path('',  views.SongListAPIView.as_view()),
    
]