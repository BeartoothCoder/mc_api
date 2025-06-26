from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='index'),
    path('<int:id>/', views.recipe_detail, name='detail'),
    path('random/', views.recipe_random, name='random'),
]
