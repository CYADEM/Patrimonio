# noticias/urls.py
from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ver_noticias, name='ver_noticias'),
    path('crear_noticia/', views.crear_noticia, name='crear_noticia'),
    path('noticias_solicitadas/', views.noticias_solicitadas, name='noticias_solicitadas'),
    # urls.py
    path('aprobar/<int:id>/', views.aprobar_noticia, name='aprobar_noticia'),
    path('rechazar/<int:id>/', views.rechazar_noticia, name='rechazar_noticia'),
    path('editar/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar/<int:id>/', views.eliminar_noticia, name='eliminar_noticia')

    # Agrega más rutas aquí si es necesario
]
