from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    fecha_nac = models.DateTimeField()

class Lector(Persona):
    estado = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Autor(Persona):
    nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    editorial = models.CharField(max_length=200)
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField()    
    fecha_devolucion = models.DateTimeField()
    multa = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Libro: {self.id_libro} - Lector: {self.id_lector}'
