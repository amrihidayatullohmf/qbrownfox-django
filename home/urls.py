from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='indexhome'),
    path('guestbook', views.guestbook, name="guestbook"),
]
