from django.urls import path
from . import views

app_name = 'slt'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), #<int:question_id> -> <int:pk>
    path('<int:question_id>/results/', views.results, name='results'), #<int:question_id> -> <int:pk>
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('test/', views.test, name='test'),
]