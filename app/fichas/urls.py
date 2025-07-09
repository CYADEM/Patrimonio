from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
    path('cargar/', views.cargar_ficha, name='cargar_ficha'),
    path('', views.lista_fichas, name='lista_fichas'),
    path('<int:ficha_id>/', views.ficha_detalle, name='ficha_detalle'),
    path('eliminar/', views.eliminar_fichas, name='eliminar_fichas'),

]
