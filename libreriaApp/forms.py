from django import forms

class CrearLibro(forms.Form):
    titulo = forms.CharField(label="Título:", max_length=200)
    tipo = forms.CharField(label="Género:", max_length=200)
    editorial = forms.CharField(label="Editorial:", max_length=200)
    anio = forms.DateField(label="Año de publicado:")

class CrearLector(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=200)
    direccion = forms.CharField(label="Dirección:", max_length=200)
    telefono = forms.CharField(label="Teléfono:", max_length=200)
    fecha_nac = forms.DateField(label="Fecha de nacimiento:")
    # (Habilitado/Inhabilitado)
    estado = forms.CharField(label="Estado:", max_length=200)

class CrearAutor(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=200)
    direccion = forms.CharField(label="Dirección:", max_length=200)
    telefono = forms.CharField(label="Teléfono:", max_length=200)
    fecha_nac = forms.DateField(label="Fecha de nacimiento:")
    nacionalidad = forms.CharField(label="Nacionalidad:", max_length=200)
