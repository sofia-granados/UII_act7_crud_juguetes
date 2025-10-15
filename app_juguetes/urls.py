from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('juguetes/<int:id>/', views.ver_juguetes, name='ver_juguetes'),
    path('juguetes/agregar/', views.agregar_juguetes, name='agregar_juguetes'),
    path('juguetes/editar/<int:id>/', views.editar_juguetes, name='editar_juguetes'),
    path('juguetes/borrar/<int:id>/', views.borrar_juguetes, name='borrar_juguetes'),
]