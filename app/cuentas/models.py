from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

# ---- Mantener CustomUser tal cual ----
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=False)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    area = models.CharField(max_length=50, choices=[
        ('Historia', 'Historia'),
        ('Bellas Artes', 'Bellas Artes'),
        ('Antropología', 'Antropología'),
        ('Staff', 'Staff')
    ], blank=True, null=True)
    
    admitido = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='customuser_permissions', blank=True
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:  # Solo superusuarios no necesitan área
           self.area = None
           self.is_staff = True 
        elif self.area == "Staff":  
            self.is_staff = True
        else:
            self.is_staff = False
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre or 'Sin nombre'} {self.apellido or ''} ({self.username})"


# ---- Noticias ----
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    portada = models.ImageField(upload_to='noticias_portadas/', null=True, blank=True)

    def __str__(self):
        return self.titulo


# ---- Área: si querés que sea dinámica, mantén este modelo ----
class Area(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


# ---- Colección ----
class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='colecciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


# ---- Campo (headers o atributos de cada colección) ----
class Campo(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, related_name='campos')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.coleccion.nombre})"


# ---- Item ----
class Item(models.Model):
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    datos = models.JSONField()  # Diccionario con clave=nombre del campo, valor=dato
    privado = models.BooleanField(default=False)
    def __str__(self):
        return f"Item en {self.coleccion.nombre}"

    class Meta:
        permissions = [
            # Si querés un permiso custom adicional, por ejemplo:
            # ('toggle_privado', 'Puede cambiar el estado privado del item'),
        ]