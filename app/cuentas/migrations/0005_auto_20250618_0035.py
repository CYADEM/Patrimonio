from django.db import migrations

def crear_areas_iniciales(apps, schema_editor):
    Area = apps.get_model('cuentas', 'Area')  # cambiá 'cuentas' por el nombre de tu app
    areas = ['Historia', 'bellas_artes']
    for nombre in areas:
        Area.objects.get_or_create(nombre=nombre)

class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),  # la migración anterior
    ]

    operations = [
        migrations.RunPython(crear_areas_iniciales),
    ]
