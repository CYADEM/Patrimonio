from django.shortcuts import render, redirect, get_object_or_404
from .forms import FichaForm
from .models import Ficha
from django.contrib import messages  # para mensaje de éxito

# Vista para cargar nueva ficha
def cargar_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            ficha = form.save()
            # Redirigimos al detalle con un mensaje
            return redirect('fichas:ficha_detalle', ficha_id=ficha.id)
    else:
        form = FichaForm()
    return render(request, 'fichas/formulario.html', {'form': form})

# Vista para mostrar/editar ficha
def ficha_detalle(request, ficha_id):
    ficha = get_object_or_404(Ficha, id=ficha_id)

    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'fichas/ficha_detalle.html', {
                'form': form,
                'ficha': ficha,
                'guardado_exitoso': True  # ← Bandera para mostrar cartel
            })
    else:
        form = FichaForm(instance=ficha)

    return render(request, 'fichas/ficha_detalle.html', {'form': form, 'ficha': ficha

    })

# Vista para tabla resumen
def lista_fichas(request):
    fichas = Ficha.objects.all().order_by('-id')
    return render(request, 'fichas/lista_fichas.html', {'fichas': fichas})


def eliminar_fichas(request):
    if request.method == 'POST':
        ids = request.POST.getlist('fichas_seleccionadas')
        Ficha.objects.filter(id__in=ids).delete()
        messages.success(request, "Ficha(s) eliminada(s) correctamente.")
    return redirect('lista_fichas')
