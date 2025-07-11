# Generated by Django 5.2.3 on 2025-06-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='aprobada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
