from django.contrib import admin
from .models import Persona, Lector, Autor, Libro, Prestamo

# Register your models here.
# admin.site.register(Persona)
admin.site.register(Lector)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)
