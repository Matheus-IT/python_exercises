from django.urls import path

from numeros import views

urlpatterns = [
    path('', views.start_game_view),
    path('tentativa/', views.tentativa_view),
]
