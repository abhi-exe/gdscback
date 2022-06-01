from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='loginroute'),
    path('mynotes',views.notelist, name='noteshomeroute'),
    path('mynotes/<int:pk>/',views.viewnote, name='singlenote'),
    path('createnote',views.newnote, name='newnote'),
]