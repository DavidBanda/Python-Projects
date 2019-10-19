from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.home, name='home-videostream'),
    path('streamvideo/', views.index, name='video-videostream'),
    path('', views.login, name='home-videostream'),
]