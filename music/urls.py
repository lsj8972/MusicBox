from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.MusicModelView.as_view(), name='index'),
    path('music/', views.MusicList.as_view(), name='music_list'),
    path('artist/', views.ArtistList.as_view(), name='artist_list'),
    path('entertainment/', views.EntertainmentList.as_view(), name='entertainment_list'),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name='music_detail'),
    path('artist/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('entertainment/<int:pk>/', views.EntertainmentDetail.as_view(), name='entertainment_detail'),
]