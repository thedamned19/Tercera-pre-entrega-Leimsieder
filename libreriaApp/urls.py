from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('libros/', views.libros, name="libros"),
    path('crear_libro/', views.crear_libro, name="crear_libro"),
    path('crear_lector/', views.crear_lector, name="crear_lector"),
    path('lectores/', views.lectores, name="lectores"),
    path('crear_autor/', views.crear_autor, name="crear_autor"),
    path('autores/', views.autores, name="autores"),
    path('prestamos/', views.prestamos, name="prestamos"),
    # path('busquedaLibro/',views.busquedaLibro, name="buscar"),
    path('busquedaLibro/',views.busquedaLibro, name="busquedaLibro"),
    path('busquedaLibro/buscar/',views.buscar, name="buscar")
]