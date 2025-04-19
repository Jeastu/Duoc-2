from django.shortcuts import render, redirect, get_object_or_404
from .data.cards_data import cards_data
from .data.pueblos_data import pueblos_data
from .data.ubicaciones_especificas_data import ubicaciones_especificas_data
from .data.ubicaciones_variadas_data import ubicaciones_variadas_data
from .data.enemigos_data import enemigos_data
from .data.armas_data import armas_data
from .data.flora_data import flora_data
from .data.consumibles_data import consumibles_data
from .data.historia_data import historia_slider, historia_texto
from .data.micuentatf_data import micuentatf_data
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import update_session_auth_hash

from .forms import CustomUserCreationForm
from .forms import ConstruccionForm
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth import logout
import re

# Importación de Modelos
from .models import Construccion
from .models import Enemigo
from .models import Planta
from .models import Animal
from .models import Pueblo, UbicacionEspecifica, UbicacionVariada
from .models import Arma
from .models import Consumible
from .models import Historia

from .forms import AnimalForm
from django.contrib.auth.decorators import user_passes_test
from .forms import PuebloForm, UbicacionEspecificaForm, UbicacionVariadaForm
from .forms import EnemigoForm
from .forms import PlantaForm
from .forms import ArmaForm
from .forms import ConsumibleForm
from .forms import HistoriaForm
from .forms import UserUpdateForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comentario
from .forms import ComentarioForoForm


@login_required
def enemigos(request):
    enemigos = Enemigo.objects.all()
    return render(request, "Enemigos.html", {"enemigos": enemigos})


@login_required
def home(request):
    return render(request, "menuprincipal_wiki.html", {"cards": cards_data})

@login_required
def animales(request):
    edit_mode = request.GET.get("edit") == "true"
    animales = Animal.objects.all()
    return render(request, "Animales.html", {
        "animales": animales,
        "edit_mode": edit_mode
    })


@login_required
def lugarestf(request):
    pueblos = Pueblo.objects.all()
    especificas = UbicacionEspecifica.objects.all()
    variadas = UbicacionVariada.objects.all()

    return render(request, "Lugarestf.html", {
        "pueblos": pueblos,
        "ubicaciones_especificas": especificas,
        "ubicaciones_variadas": variadas
    })

@login_required
def enemigos(request):
    enemigos = Enemigo.objects.all()
    return render(request, "Enemigos.html", {"enemigos": enemigos})

@login_required
def construcciones(request):
    construcciones = Construccion.objects.all()
    return render(request, "Construcciones.html", {"construcciones": construcciones})


@login_required
def flora(request):
    plantas = Planta.objects.all()
    return render(request, "Flora.html", {"plantas": plantas})



@login_required
def armas(request):
    armas = Arma.objects.all()
    return render(request, "Armas.html", {"armas": armas})

@login_required
def consumibles(request):
    consumibles = Consumible.objects.all()
    return render(request, "Consumibles.html", {"consumibles": consumibles})

@login_required
def historia(request):
    texto = Historia.objects.filter(texto__isnull=False).first()
    imagenes = Historia.objects.filter(imagen__isnull=False)
    return render(request, "historia.html", {
        "historia_texto": texto,
        "historia_slider": imagenes
    })

@login_required
def forowiki(request):
    return render(request, "forowiki.html")


def inicio_sesion_wiki(request):
    return render(request, "inicio_sesion_wiki.html")





















@login_required
def micuentatf(request):
    edit_mode = request.GET.get("edit") == "true"
    change_password = request.GET.get("change_password") == "true"

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        current_password = request.POST.get("current_password")

        if not request.user.check_password(current_password):
            messages.error(request, "Contraseña actual incorrecta.")
            return HttpResponseRedirect(reverse("micuentatf") + "?edit=true&change_password=true")

        if form.is_valid():
            user = form.save()

            # Verifica si se quieren cambiar las contraseñas
            new_pass1 = request.POST.get("new_password1")
            new_pass2 = request.POST.get("new_password2")

            if new_pass1 or new_pass2:
                if new_pass1 != new_pass2:
                    messages.error(request, "Las contraseñas no coinciden.")
                    url = reverse("micuentatf") + "?edit=true&change_password=true"
                    return HttpResponseRedirect(url)
                else:
                    user.set_password(new_pass1)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Datos y contraseña actualizados correctamente.")
            else:
                user.save()
                messages.success(request, "Datos actualizados correctamente.")

            return redirect("micuentatf")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "micuentatf.html", {
        "micuenta": request.user,
        "form": form,
        "edit_mode": edit_mode,
        "change_password": change_password
    })





















def recuperarcontra(request):
    return render(request, "recuperarcontra.html")


def registrase(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada exitosamente!")
            return redirect("home")
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = CustomUserCreationForm()

    return render(request, "registrase_wiki.html", {"form": form})


from django.contrib.auth import authenticate, login


def inicio_sesion_wiki(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "inicio_sesion_wiki.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio_sesion_wiki")

@user_passes_test(lambda u: u.is_staff)
def eliminar_construccion(request, pk):
    construccion = get_object_or_404(Construccion, pk=pk)
    construccion.delete()
    messages.success(request, "Construcción eliminada correctamente.")
    return redirect('construcciones')

@user_passes_test(lambda u: u.is_staff)
def editar_construccion(request, id):
    construccion = get_object_or_404(Construccion, id=id)

    if request.method == 'POST':
        form = ConstruccionForm(request.POST, request.FILES, instance=construccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Construcción actualizada correctamente.')
            return redirect('construcciones')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = ConstruccionForm(instance=construccion)

    return render(request, 'editar_construccion.html', {'form': form, 'construccion': construccion})



# agregado de clima_chile

import requests
from django.contrib.auth.decorators import login_required

@login_required
def clima_chile(request):
    regiones = {
        "arica y parinacota": {"lat": -18.478, "lon": -70.3126},
        "tarapacá": {"lat": -20.2133, "lon": -70.1525},
        "antofagasta": {"lat": -23.6524, "lon": -70.3954},
        "atacama": {"lat": -27.3668, "lon": -70.3314},
        "coquimbo": {"lat": -29.9533, "lon": -71.3395},
        "valparaíso": {"lat": -33.0472, "lon": -71.6127},
        "metropolitana": {"lat": -33.4489, "lon": -70.6693},
        "ohiggins": {"lat": -34.1708, "lon": -70.7406},
        "maule": {"lat": -35.4264, "lon": -71.6554},
        "ñuble": {"lat": -36.6063, "lon": -72.1034},
        "biobío": {"lat": -36.8201, "lon": -73.0444},
        "araucanía": {"lat": -38.7359, "lon": -72.5904},
        "los rios": {"lat": -39.8142, "lon": -73.2459},
        "los lagos": {"lat": -41.4717, "lon": -72.9396},
        "aysén": {"lat": -45.571, "lon": -72.068},
        "magallanes": {"lat": -53.1625, "lon": -70.9081},
    }

    region = request.GET.get("region", "metropolitana").lower()
    coords = regiones.get(region, regiones["metropolitana"])

    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
        response = requests.get(url)
        data = response.json()["current_weather"]
        contexto = {
            "region": region.title(),
            "regiones": regiones,
            "temperatura": data["temperature"],
            "viento": data["windspeed"],
            "clima_codigo": data["weathercode"],
        }
    except:
        contexto = {
            "error": "No se pudo obtener el clima",
            "regiones": regiones
        }

    return render(request, "clima_chile.html", contexto)



@user_passes_test(lambda u: u.is_staff)
def editar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal actualizado correctamente.')
            return redirect('animales')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'editar_animal.html', {'form': form, 'animal': animal})


@user_passes_test(lambda u: u.is_staff)
def editar_pueblo(request, id):
    pueblo = get_object_or_404(Pueblo, id=id)

    if request.method == 'POST':
        form = PuebloForm(request.POST, instance=pueblo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pueblo actualizado correctamente.')
            return redirect('lugarestf')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = PuebloForm(instance=pueblo)

    return render(request, 'editar_pueblo.html', {'form': form, 'pueblo': pueblo})



@user_passes_test(lambda u: u.is_staff)
def editar_ubicacion_especifica(request, id):
    ubicacion = get_object_or_404(UbicacionEspecifica, id=id)

    if request.method == 'POST':
        form = UbicacionEspecificaForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ubicación específica actualizada correctamente.')
            return redirect('lugarestf')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = UbicacionEspecificaForm(instance=ubicacion)

    return render(request, 'editar_ubicacion_especifica.html', {'form': form, 'ubicacion': ubicacion})


@user_passes_test(lambda u: u.is_staff)
def editar_ubicacion_variada(request, id):
    ubicacion = get_object_or_404(UbicacionVariada, id=id)

    if request.method == 'POST':
        form = UbicacionVariadaForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ubicación variada actualizada correctamente.')
            return redirect('lugarestf')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = UbicacionVariadaForm(instance=ubicacion)

    return render(request, 'editar_ubicacion_variada.html', {'form': form, 'ubicacion': ubicacion})



@user_passes_test(lambda u: u.is_staff)
def editar_enemigo(request, id):
    enemigo = get_object_or_404(Enemigo, id=id)

    if request.method == 'POST':
        form = EnemigoForm(request.POST, instance=enemigo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enemigo actualizado correctamente.')
            return redirect('enemigos')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = EnemigoForm(instance=enemigo)

    return render(request, 'editar_enemigo.html', {'form': form, 'enemigo': enemigo})


@user_passes_test(lambda u: u.is_staff)
def editar_planta(request, id):
    planta = get_object_or_404(Planta, id=id)

    if request.method == 'POST':
        form = PlantaForm(request.POST, instance=planta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Planta actualizada correctamente.')
            return redirect('flora')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = PlantaForm(instance=planta)

    return render(request, 'editar_planta.html', {'form': form, 'planta': planta})


@user_passes_test(lambda u: u.is_staff)
def editar_arma(request, id):
    arma = get_object_or_404(Arma, id=id)

    if request.method == 'POST':
        form = ArmaForm(request.POST, request.FILES, instance=arma)
        if form.is_valid():
            form.save()
            messages.success(request, 'Arma actualizada correctamente.')
            return redirect('armas')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = ArmaForm(instance=arma)

    return render(request, 'editar_arma.html', {'form': form, 'arma': arma})



@user_passes_test(lambda u: u.is_staff)
def editar_consumible(request, id):
    consumible = get_object_or_404(Consumible, id=id)

    if request.method == 'POST':
        form = ConsumibleForm(request.POST, instance=consumible)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consumible actualizado correctamente.')
            return redirect('consumibles')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = ConsumibleForm(instance=consumible)

    return render(request, 'editar_consumible.html', {
        'form': form,
        'consumible': consumible
    })


@user_passes_test(lambda u: u.is_staff)
def editar_historia(request, id):
    historia = get_object_or_404(Historia, id=id)

    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES, instance=historia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historia actualizada correctamente.')
            return redirect('historia')
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = HistoriaForm(instance=historia)

    return render(request, 'editar_historia.html', {'form': form, 'historia': historia})


def validar_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

@login_required
def micuentatf(request):
    edit_mode = request.GET.get("edit") == "true"
    change_password = request.GET.get("change_password") == "true"

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        current_password = request.POST.get("current_password")

        if not request.user.check_password(current_password):
            messages.error(request, "Contraseña actual incorrecta.")
            return redirect("micuentatf")

        if form.is_valid():
            user = form.save()

            # Verifica si se quieren cambiar las contraseñas
            new_pass1 = request.POST.get("new_password1")
            new_pass2 = request.POST.get("new_password2")

            if new_pass1 or new_pass2:
                if new_pass1 != new_pass2:
                    messages.error(request, "Las contraseñas no coinciden.")
                    return HttpResponseRedirect(reverse("micuentatf") + "?edit=true&change_password=true")

                elif not validar_password(new_pass1):
                    messages.error(request, "La nueva contraseña no cumple con los requisitos: al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo.")
                    return HttpResponseRedirect(reverse("micuentatf") + "?edit=true&change_password=true")

                else:
                    user.set_password(new_pass1)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Datos y contraseña actualizados correctamente.")
            else:
                user.save()
                messages.success(request, "Datos actualizados correctamente.")

            return redirect("micuentatf")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "micuentatf.html", {
        "micuenta": request.user,
        "form": form,
        "edit_mode": edit_mode,
        "change_password": change_password
    })





from .forms import EmailRecoveryForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
def recuperarcontra(request):
    mensaje = ""
    if request.method == "POST":
        form = EmailRecoveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            mensaje = f"✅ Se ha enviado un correo a {email}"
        else:
            mensaje = "❌ Correo inválido"
    else:
        form = EmailRecoveryForm()

    return render(request, "recuperarcontra.html", {
        "form": form,
        "mensaje": mensaje
    })




from django.http import JsonResponse

@login_required
def api_animales(request):
    animales = Animal.objects.all().values('id', 'nombre', 'descripcion', 'imagen')
    return JsonResponse(list(animales), safe=False)

@login_required
def api_lugarestf(request):
    data = {
        'pueblos': list(Pueblo.objects.all().values('id', 'nombre', 'descripcion', 'imagen')),
        'ubicaciones_especificas': list(UbicacionEspecifica.objects.all().values('id', 'nombre', 'descripcion', 'imagen')),
        'ubicaciones_variadas': list(UbicacionVariada.objects.all().values('id', 'nombre', 'descripcion', 'imagen'))
    }
    return JsonResponse(data, safe=False)

@login_required
def api_enemigos(request):
    enemigos = Enemigo.objects.all().values('id', 'nombre', 'descripcion', 'imagen')
    return JsonResponse(list(enemigos), safe=False)

@login_required
def api_construcciones(request):
    construcciones = Construccion.objects.all().values('id', 'nombre', 'materiales', 'descripcion', 'imagen')
    return JsonResponse(list(construcciones), safe=False)

@login_required
def api_plantas(request):
    plantas = Planta.objects.all().values('id', 'nombre', 'tipo', 'descripcion', 'imagen')
    return JsonResponse(list(plantas), safe=False)

@login_required
def api_armas(request):
    armas = Arma.objects.all().values('id', 'numero', 'nombre', 'tipo', 'descripcion', 'imagen')
    return JsonResponse(list(armas), safe=False)

@login_required
def api_consumibles(request):
    consumibles = Consumible.objects.all().values(
        'id', 'nombre', 'imagen',
        'hambre_normal', 'agua_normal', 'vida_normal', 'energia_normal',
        'hambre_dificil', 'agua_dificil', 'vida_dificil', 'energia_dificil'
    )
    return JsonResponse(list(consumibles), safe=False)

@login_required
def api_historia(request):
    historia = Historia.objects.all().values('id', 'imagen', 'texto')
    return JsonResponse(list(historia), safe=False)





from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Comentario

@login_required
def forowiki(request):
    if request.method == "POST":
        if "borrar_id" in request.POST:
            comentario_id = request.POST.get("borrar_id")
            comentario = get_object_or_404(Comentario, id=comentario_id)
            if request.user == comentario.usuario or request.user.is_staff:
                comentario.delete()
                messages.success(request, "Comentario eliminado.")
        else:
            form = ComentarioForoForm(request.POST)
            if form.is_valid():
                nuevo_comentario = form.save(commit=False)
                nuevo_comentario.usuario = request.user
                nuevo_comentario.save()
                messages.success(request, "Comentario publicado.")
        return redirect("forowiki")

    comentarios = Comentario.objects.all().order_by("-fecha")
    form = ComentarioForoForm()
    return render(request, "forowiki.html", {
        "comentarios": comentarios,
        "form": form
    })







from django.shortcuts import redirect
from .models import Comentario
from .forms import ComentarioForoForm
from django.contrib.auth.decorators import login_required

@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)

    if request.user != comentario.usuario and not request.user.is_staff:
        return redirect('forowiki')

    if request.method == "POST":
        form = ComentarioForoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('forowiki')
    else:
        form = ComentarioForoForm(instance=comentario)

    return render(request, "editar_comentario.html", {"form": form})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario
from .forms import ComentarioForoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)

    # Solo el autor o el staff puede editar
    if request.user != comentario.usuario and not request.user.is_staff:
        messages.error(request, "No tienes permiso para editar este comentario.")
        return redirect("forowiki")

    if request.method == "POST":
        form = ComentarioForoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario actualizado.")
            return redirect("forowiki")
    else:
        form = ComentarioForoForm(instance=comentario)

    return render(request, "editar_comentario.html", {"form": form, "comentario": comentario})




@login_required
def borrar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)

    # Solo el autor o el staff puede borrar
    if request.user != comentario.usuario and not request.user.is_staff:
        messages.error(request, "No tienes permiso para borrar este comentario.")
        return redirect("forowiki")

    comentario.delete()
    messages.success(request, "Comentario eliminado.")
    return redirect("forowiki")
