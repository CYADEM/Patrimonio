from django.shortcuts import get_object_or_404,render, redirect
from .forms import NoticiaForm
from .models import Noticia

# Create your views here.

app_name = "noticias"

def vista_admin(request):
    # Contamos cuántas noticias están solicitadas
    solicitud_count = Noticia.objects.filter(aprobada=False).count()

    # Pasamos la cantidad de solicitudes al contexto
    context = {
        'solicitud_count': solicitud_count,
    }

    return render(request, 'base.html', context)

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.aprobada = False  # <-- aquí
            noticia.save()
            return redirect('noticias:crear_noticia')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/crearnuevanoticia.html', {'form': form})

def ver_noticias(request):
    noticias = Noticia.objects.filter(aprobada=True).order_by('-fecha_publicacion')
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def noticias_solicitadas(request):
    #noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    noticias = Noticia.objects.filter(aprobada=False).order_by('-fecha_publicacion')
    return render(request, 'noticias/solicitudes.html', {'noticias': noticias})


def aprobar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.aprobada = True
    noticia.save()
    noticias = Noticia.objects.filter(aprobada=False).order_by('-fecha_publicacion')
    return render(request, 'noticias/solicitudes.html', {'noticias': noticias})  # O donde quieras redirigir

def rechazar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.delete()
    noticias = Noticia.objects.filter(aprobada=False).order_by('-fecha_publicacion')
    return render(request, 'noticias/solicitudes.html', {'noticias': noticias})  # O donde quieras redirigir

def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.delete()
    noticias = Noticia.objects.filter(aprobada=False).order_by('-fecha_publicacion')
    return render(request, 'noticias/solicitudes.html', {'noticias': noticias})  # O donde quieras redirigir

def editar_noticia(request, id):
    # Podés hacer un formulario más adelante
    return redirect('noticias_solicitadas')


def noticias_home(request):
    noticias = Noticia.objects.filter(aprobada=True)
    solicitudes_pendientes = Noticia.objects.filter(aprobada=False)
    return render(request, 'noticias/noticias.html', {
        'noticias': noticias,
        'hay_solicitudes': solicitudes_pendientes.exists()
    })