# 📌 Imports organizados y únicos
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
import pandas as pd
import math
from django.core.paginator import Paginator


from .models import (
    CustomUser, Noticia, Area, Coleccion, Campo, Item
)
from .forms import CrearColeccionForm


# 📌 Vistas básicas
def home(request):
    return render(request, 'pages/home.html')


# 📌 Autenticación y acceso
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(request, username=username, password=password)

        if user:
            # Validar permisos
            if user.is_superuser or user.is_staff or user.admitido:
                login(request, user)
                request.session.save()
                return redirect(reverse("cuentas:colecciones"))
            else:
                return render(request, "auth/login.html", {
                    "error_message": "Acceso denegado. Usuario no admitido."
                })
        else:
            return render(request, "auth/login.html", {
                "error_message": "Usuario o contraseña incorrectos."
            })

    return render(request, "auth/login.html")


@login_required
def colecciones(request):
    if not (request.user.is_superuser or request.user.is_staff or request.user.admitido):
        return render(request, 'access_denied.html')

    pending_users = CustomUser.objects.filter(admitido=False).count()

    return render(request, 'users/colecciones.html', {
        'user': request.user,
        'pending_users': pending_users
    })


# 📌 Registro de usuarios
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        nombre = request.POST.get('nombre').strip()
        apellido = request.POST.get('apellido').strip()
        email = request.POST.get('email').strip()
        area = request.POST.get('area')
        password = request.POST.get('password')

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {
                'error_message': 'El nombre de usuario ya está en uso. Prueba otro.'
            })

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {
                'error_message': 'El correo electrónico ya está registrado. Usa otro.'
            })

        user = CustomUser(
            username=username,
            nombre=nombre,
            apellido=apellido,
            email=email,
            area=area
        )
        user.set_password(password)

        if area == "Staff":
            user.is_staff = True

        user.save()

        return redirect('/')

    return render(request, 'auth/register.html')


# 📌 Gestión de usuarios
@login_required
def users(request):
    users = CustomUser.objects.all()
    users_admitidos = users.filter(admitido=True)
    users_no_admitidos = users.filter(admitido=False)

    areas_dict = {}
    for user in users_admitidos:
        area = user.area if user.area else "Sin asignar"
        if area not in areas_dict:
            areas_dict[area] = []
        areas_dict[area].append(user)

    return render(request, "users/users_list.html", {
        "users_no_admitidos": users_no_admitidos,
        "areas_dict": areas_dict
    })


@login_required
def admit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.admitido = True
        user.save()
    return redirect('cuentas:users')


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect(reverse("cuentas:users"))


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.nombre = request.POST.get("nombre")
        user.apellido = request.POST.get("apellido")
        user.email = request.POST.get("email")
        user.area = request.POST.get("area")

        user.is_staff = (request.POST.get("area") == "Staff") or request.POST.get("is_staff") == "on"

        user.save()
        return redirect("cuentas:users")

    return render(request, "fichas/edit_user.html", {"user": user})


@login_required
def update_password(request):
    user = request.user

    if request.method == 'POST':
        old_password = request.POST.get('old_password').strip()
        new_password = request.POST.get('new_password').strip()
        confirm_password = request.POST.get('confirm_password').strip()

        if not old_password or not new_password or not confirm_password:
            return render(request, 'auth/update_password.html', {
                'error_message': 'Todos los campos son obligatorios.'
            })

        if not user.check_password(old_password):
            return render(request, 'auth/update_password.html', {
                'error_message': 'Contraseña actual incorrecta.'
            })

        if len(new_password) < 8 or new_password != confirm_password:
            return render(request, 'auth/update_password.html', {
                'error_message': 'Contraseña inválida.'
            })

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)

        return redirect('cuentas:colecciones')

    return render(request, 'auth/update_password.html')


# 📌 Noticias
def noticias_view(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'auth/news.html', {"noticias": noticias})


def obtener_noticias(request):
    noticias_json = [
        {
            "id": noticia.id,
            "titulo": noticia.titulo,
            "contenido": noticia.contenido[:200],
            "fecha": noticia.fecha_publicacion.strftime("%Y-%m-%d"),
            "portada": noticia.portada.url if noticia.portada else ""
        }
        for noticia in Noticia.objects.all().order_by('-fecha_publicacion')
    ]
    return JsonResponse(noticias_json, safe=False)


@login_required
def cargar_noticias_view(request):
    return render(request, 'fichas/cargar_noticias.html')


from cuentas.models import Area, Coleccion

def bellas_artes(request):
    area = Area.objects.get(nombre='bellas_artes')
    colecciones = Coleccion.objects.filter(area=area)
    return render(request, 'pages/bellas_artes.html', {
        'colecciones': colecciones
    })



@login_required
def historia(request):
    historia_area = Area.objects.filter(nombre__iexact="Historia").first()
    colecciones = historia_area.colecciones.all() if historia_area else []
    return render(request, 'pages/historia.html', {'colecciones': colecciones})


def antropologia(request):
    return render(request, 'pages/antropologia.html')


def formularioAntropologia(request):
    return render(request, 'fichas/formularioAntropologia.html')


# 📌 Crear colección con campos dinámicos
@login_required
def crear_coleccion(request, area):
    area_obj = get_object_or_404(Area, nombre__iexact=area)

    if request.method == "POST":
        form = CrearColeccionForm(request.POST)
        archivo_excel = request.FILES.get('archivo')

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            campos_str = form.cleaned_data['campos']
            lista_campos = [campo.strip() for campo in campos_str.split(',') if campo.strip()]

            coleccion = Coleccion.objects.create(nombre=nombre, area=area_obj)

            for campo_nombre in lista_campos:
                Campo.objects.create(coleccion=coleccion, nombre=campo_nombre)

            # Si se subió un archivo Excel, procesarlo para crear Items
            if archivo_excel:
                df = pd.read_excel(archivo_excel)
                filas = df.values.tolist()
                # Usamos lista_campos para crear los datos
                for fila in filas:
                    datos = dict(zip(lista_campos, fila))
                    Item.objects.create(coleccion=coleccion, datos=datos)

            return redirect(f'cuentas:{area.lower()}')
    else:
        form = CrearColeccionForm()

    return render(request, 'pages/crear_coleccion.html', {
        'form': form,
        'area': area_obj
    })


def limpiar_fila(fila):
    fila_limpia = {}
    for k, v in fila.items():
        if v is None:
            fila_limpia[k] = None
        elif isinstance(v, float) and math.isnan(v):
            fila_limpia[k] = None
        else:
            fila_limpia[k] = v
    return fila_limpia


@login_required
def detalle_coleccion(request, pk):
    coleccion = get_object_or_404(Coleccion, id=pk)
    campos = coleccion.campos.all()

    items_excel = None
    columnas_excel = None
    items_db = None
    
    # Editar nombre de la colección
    if request.method == "POST" and request.POST.get('actualizar_nombre_coleccion'):
        nuevo_nombre = request.POST.get('nombre_coleccion', '').strip()
        if nuevo_nombre:
            coleccion.nombre = nuevo_nombre
            coleccion.save()
            messages.success(request, "Nombre de la colección actualizado.")
        else:
            messages.error(request, "El nombre de la colección no puede estar vacío.")
        return redirect(request.path)
    

    # Borrar item
    if request.method == "POST" and 'borrar_item_id' in request.POST:
        item_id = request.POST.get('borrar_item_id')
        try:
            item = Item.objects.get(id=item_id, coleccion=coleccion)
            item.delete()
            messages.success(request, "Ítem borrado correctamente.")
        except Item.DoesNotExist:
            messages.error(request, "Ítem no encontrado para borrar.")
        return redirect(request.path)

    # Importar archivo Excel
    if request.method == "POST" and 'archivo_excel' in request.FILES:
        archivo_excel = request.FILES['archivo_excel']
        df = pd.read_excel(archivo_excel)

        columnas_excel = df.columns.tolist()
        items_excel = df.to_dict(orient='records')

        coleccion.campos.all().delete()
        coleccion.items.all().delete()
        
        for campo_nombre in columnas_excel:
            Campo.objects.create(coleccion=coleccion, nombre=campo_nombre)

        request.session['datos_temporales'] = {
            'columnas_excel': columnas_excel,
            'items_excel': items_excel,
        }
        messages.success(request, "Archivo Excel importado y campos actualizados.")

    # Guardar datos importados o edición masiva
    elif request.method == "POST" and request.POST.get('guardar') == '1':
                # Actualizar nombre de colección si vino en el formulario
        nuevo_nombre = request.POST.get('nombre_coleccion', '').strip()
        if nuevo_nombre and nuevo_nombre != coleccion.nombre:
            coleccion.nombre = nuevo_nombre
            coleccion.save()

        datos_temporales = request.session.get('datos_temporales')

        if datos_temporales:
            # Guardar datos importados desde Excel
            columnas_excel = datos_temporales.get('columnas_excel')
            items_excel = datos_temporales.get('items_excel')

            for fila in items_excel:
                datos_limpios = limpiar_fila(fila)
                Item.objects.create(coleccion=coleccion, datos=datos_limpios)

            del request.session['datos_temporales']
            messages.success(request, "Datos guardados correctamente.")
            return redirect(request.path)

        else:
            # Procesar edición de items existentes (inputs con prefijo 'data-')
            datos_editar = {k: v for k, v in request.POST.items() if k.startswith('data-')}

            if not datos_editar:
                messages.error(request, "No hay datos para guardar. Primero importá un archivo Excel o editá los items.")
                return redirect(request.path)

            # Agrupar datos por item_id
            datos_por_item = {}

            for clave, valor in datos_editar.items():
                # clave formato: data-<itemId>-<campo>
                try:
                    _, item_id, campo = clave.split('-', 2)
                except ValueError:
                    continue

                if item_id not in datos_por_item:
                    datos_por_item[item_id] = {}
                datos_por_item[item_id][campo] = valor

            # Actualizar cada item en BD
            for item_id, datos in datos_por_item.items():
                try:
                    item_obj = Item.objects.get(id=item_id, coleccion=coleccion)
                    datos_limpios = limpiar_fila(datos)  # si usás esta función para limpiar datos
                    item_obj.datos = datos_limpios
                    item_obj.save()
                except Item.DoesNotExist:
                    continue

            messages.success(request, "Cambios guardados correctamente.")
            return redirect(request.path)

    # Crear nuevo ítem manualmente
    elif request.method == "POST" and request.POST.get('guardar_items') == '1':
        nuevo_item_data = {}
        hay_datos_nuevos = False
        for campo in campos:
            valor = request.POST.get(f'nuevo_{campo.nombre}', '').strip()
            nuevo_item_data[campo.nombre] = valor
            if valor != '':
                hay_datos_nuevos = True

        if hay_datos_nuevos:
            Item.objects.create(coleccion=coleccion, datos=nuevo_item_data)
            messages.success(request, "Nuevo ítem creado correctamente.")
        else:
            messages.info(request, "No se ingresaron datos para el nuevo ítem.")

        return redirect(request.path)

    else:
        # Aquí definís la lista completa
        items_list = coleccion.items.all()

        # Paginador: 10 items por página
        paginator = Paginator(items_list, 10)

        # Obtener número de página de la query string ?page=
        page_number = request.GET.get('page')

        # Obtener solo la página pedida
        items_db = paginator.get_page(page_number)

    nuevo_item = {campo.nombre: '' for campo in campos}

    context = {
        "coleccion": coleccion,
        "campos": campos,
        "items_excel": items_excel,
        "columnas_excel": columnas_excel,
        "items_db": items_db,
        "nuevo_item": nuevo_item,
    }
    return render(request, "pages/detalle_coleccion.html", context)



@login_required
def borrar_coleccion(request, pk):
    coleccion = get_object_or_404(Coleccion, id=pk)
    if request.method == 'POST':
        nombre = coleccion.nombre
        coleccion.delete()
        messages.success(request, f'La colección "{nombre}" fue borrada correctamente.')
    return redirect('cuentas:historia')



@require_POST
@login_required
def toggle_privacidad_ajax(request):
    item_id = request.POST.get('item_id')
    if not item_id:
        return JsonResponse({'error': 'No se proporcionó item_id'}, status=400)

    item = get_object_or_404(Item, id=item_id)

    if not request.user.has_perm('cuentas.change_item'):
        return JsonResponse({'error': 'No tienes permiso para cambiar este estado'}, status=403)

    item.privado = not item.privado
    item.save()

    return JsonResponse({'privado': item.privado})


from fichas.models import Ficha

def antropologia_view(request):
    fichas = Ficha.objects.all()
    return render(request, 'antropologia.html', {'fichas': fichas})

