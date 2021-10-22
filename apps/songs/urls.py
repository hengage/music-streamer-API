from django.urls import path

from . import views


urlpatterns = [
    path('',  views.SongListAPIView.as_view()),
    path('songs/<slug:slug>/', views.SongDetailAPIView.as_view()),
    #path('songs/<int:pk>', views.SongDetailAPIView.as_view()),
    
]