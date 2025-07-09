from django.db import models
from django.core.validators import FileExtensionValidator

class Ficha(models.Model):
    nro_id = models.IntegerField()
    sigla_cicpse = models.IntegerField()
    sigla_renicoa = models.CharField(max_length=100, blank=True)
    otros_nros = models.CharField(max_length=200, blank=True)
    nombre_coleccion = models.CharField(max_length=200)
    nombre_descriptivo = models.CharField(max_length=200, blank=True)
    tipo_material = models.CharField(max_length=100)
    anio_coleccion = models.CharField(max_length=20, blank=True)
    forma_ingreso = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    otros_datos = models.TextField(blank=True)

    # --- Datos de Procedencia ---
    pais = models.CharField(max_length=100, blank=True)
    pais_region = models.CharField(max_length=100, blank=True)
    departamento = models.CharField(max_length=100, blank=True)
    localidad = models.CharField(max_length=100, blank=True)
    sitio_arqueologico = models.CharField(max_length=200, blank=True)
    datos_contextuales = models.TextField(blank=True)

       #-----Datos del Registro-----
    fecha_registro = models.DateField(blank=True, null=True)
    nombre_apellido = models.CharField(max_length=200, blank=True)
    dni = models.IntegerField(blank=True, null=True)
    designacion = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=50, blank=True)

     # --- Descripcion del Objeto ---
    forma = models.CharField(max_length=100, blank=True)
    tecnica = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    adscripcion_cultural_temporal = models.CharField(max_length=100, blank=True)

        # --- Medidas del Objeto (en cm.) ---
    altura_largo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ancho_diametro_maximo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    espesor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    otras_alturas = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    diametro_minimo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    otras_medidas = models.CharField(max_length=200, blank=True)

        # --- ESTADO DE CONSERVACIÓN ---
    estado_conservacion = models.CharField(max_length=50, blank=True)
    estado_estructural = models.CharField(max_length=50, blank=True)
    estado_superficie = models.CharField(max_length=50, blank=True)

    deterioro_quimico = models.CharField(max_length=50, blank=True)
    deterioro_mecanico = models.CharField(max_length=50, blank=True)
    deterioro_biologico = models.CharField(max_length=50, blank=True)

    intervenciones = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)


        # --- DATOS ADICIONALES ---
    intervenciones_investigacion = models.TextField(blank=True)
    prestamos_exposiciones = models.TextField(blank=True)
    ubicaciones_anteriores = models.TextField(blank=True)
    documentacion_asociada = models.TextField(blank=True)
    asociacion_otros_lotes_objetos = models.TextField(blank=True)
    historia_objeto = models.TextField(blank=True)
    otra_informacion = models.TextField(blank=True)

   

    # --- FOTOGRAFÍAS ---
#---ImageField: permite subir una imagen y guarda su ruta---
#---upload_to='fotos/': guarda la imagen en media/fotos/---
#---blank=True, null=True: permite dejarla vacía---
#---FileExtensionValidator: valida que sea .jpg, .jpeg o .png---

    foto_sin_intervencion = models.ImageField(
        upload_to='fotos/', blank=True, null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    foto_intervenido = models.ImageField(
        upload_to='fotos/', blank=True, null=True
    )
    foto_rotulos = models.ImageField(
        upload_to='fotos/', blank=True, null=True
    )
    otras_fotografias = models.ImageField(
        upload_to='fotos/', blank=True, null=True
    )




   




    """fecha_registro = models.DateField()
    nombre_apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    designacion = models.CharField(max_length=200)
    contacto = models.CharField(max_length=50)"""

    def __str__(self):
        return f"{self.nro_id} - {self.nombre_descriptivo}"

