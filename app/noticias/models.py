from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    aprobada = models.BooleanField(default=False)  