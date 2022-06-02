from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='loginroute'),
    path('mynotes/user',views.notelist, name='noteshomeroute'),
    path('mynotes/view/<int:pk>/',views.viewnote, name='singlenote'),
    path('createnote',views.newnote, name='newnote'),
    path('mynotes/<int:pk>/edit',views.changenote, name='changenote'),
]