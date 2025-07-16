from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aulas/online/', views.aula_online, name='aula_online'),
    path('aulas/presencial/', views.aula_presencial, name='aula_presencial'),
    path('contato/', views.contato, name='contato'),
    path('eventos/', views.eventos, name='eventos'),
    path('sobre/', views.sobre, name='sobre'),
]
