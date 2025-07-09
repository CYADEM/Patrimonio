"""from django import forms
from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'"""
from django import forms
from .models import Ficha


class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = [
            # BLOQUE 1
            'nro_id', 'sigla_cicpse', 'sigla_renicoa', 'otros_nros',
            'nombre_coleccion', 'nombre_descriptivo', 'tipo_material',
            'anio_coleccion', 'forma_ingreso', 'ubicacion', 'otros_datos',

            # BLOQUE 2
            'pais', 'pais_region', 'departamento', 'localidad',
            'sitio_arqueologico', 'datos_contextuales',

            # BLOQUE 3
            'forma', 'tecnica', 'descripcion',
            'adscripcion_cultural_temporal',
            'altura_largo', 'ancho_diametro_maximo',
            'espesor', 'otras_alturas', 'diametro_minimo', 'otras_medidas',

            # BLOQUE 4
            'fecha_registro', 'nombre_apellido', 'dni',
            'designacion', 'contacto',
        ]

        labels = {
            # BLOQUE 1
            'nro_id': 'N°',
            'sigla_cicpse': 'N° de sigla CICPSE',
            'sigla_renicoa': 'Sigla RENICOA',
            'otros_nros': 'Otros N° de registro',
            'nombre_coleccion': 'Nombre de la colección',
            'nombre_descriptivo': 'Nombre descriptivo',
            'tipo_material': 'Tipo de material',
            'anio_coleccion': 'Año de colección',
            'forma_ingreso': 'Forma de ingreso',
            'ubicacion': 'Ubicación',
            'otros_datos': 'Otros datos',

            # BLOQUE 2
            'pais': 'País',
            'pais_region': 'Provincia / Región',
            'departamento': 'Departamento',
            'localidad': 'Localidad',
            'sitio_arqueologico': 'Sitio arqueológico',
            'datos_contextuales': 'Datos contextuales',

            # BLOQUE 3
            'forma': 'Forma',
            'tecnica': 'Técnica',
            'descripcion': 'Descripción',
            'adscripcion_cultural_temporal': 'Adscripción cultural / temporal',
            'altura_largo': 'Altura / Largo',
            'ancho_diametro_maximo': 'Ancho / Diámetro máx.',
            'espesor': 'Espesor',
            'otras_alturas': 'Otras alturas',
            'diametro_minimo': 'Diámetro mínimo',
            'otras_medidas': 'Otras medidas',

            # BLOQUE 4
            'fecha_registro': 'Fecha del registro',
            'nombre_apellido': 'Nombre y apellido',
            'dni': 'DNI',
            'designacion': 'Designación',
            'contacto': 'Contacto',
        }

        widgets = {
            # BLOQUE 1
            'nro_id': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'sigla_cicpse': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'sigla_renicoa': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'otros_nros': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'nombre_coleccion': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'nombre_descriptivo': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'tipo_material': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'anio_coleccion': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'forma_ingreso': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'ubicacion': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'otros_datos': forms.Textarea(attrs={'rows': 3, 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),

            # BLOQUE 2
            'pais': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'pais_region': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'departamento': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'localidad': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'sitio_arqueologico': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'datos_contextuales': forms.Textarea(attrs={'rows': 3, 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),

            # BLOQUE 3
            'forma': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'tecnica': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'adscripcion_cultural_temporal': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'altura_largo': forms.NumberInput(attrs={'step': '0.01', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'ancho_diametro_maximo': forms.NumberInput(attrs={'step': '0.01', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'espesor': forms.NumberInput(attrs={'step': '0.01', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'otras_alturas': forms.NumberInput(attrs={'step': '0.01', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'diametro_minimo': forms.NumberInput(attrs={'step': '0.01', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'otras_medidas': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),

            # BLOQUE 4
            'fecha_registro': forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'nombre_apellido': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'dni': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'designacion': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
            'contacto': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2'}),
        }
