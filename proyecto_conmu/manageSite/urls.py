from django.urls import path
from manageSite import views

urlpatterns = [
    path('', views.index, name='manageSite-index'),
    path('streamvideo/', views.video, name='video-videostream'),
    path('eliminar-usuario/', views.eliminar, name='manageSite-eliminar'),
    path('grabaciones/', views.grabacion, name='manageSite-grabacion'),
    path('monitorear/', views.monitoreo, name='manageSite-monitoreo'),
    path('Pruebamonitoreo/', views.Pruebamonitoreo, name='manageSite-Pruebamonitoreo'),
]

