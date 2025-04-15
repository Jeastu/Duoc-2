from django.shortcuts import render, redirect, get_object_or_404
from .data.cards_data import cards_data
from .data.pueblos_data import pueblos_data
from .data.ubicaciones_especificas_data import ubicaciones_especificas_data
from .data.ubicaciones_variadas_data import ubicaciones_variadas_data
from .data.animales_data import animales_data
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


# Importación de Modelos
from .models import Construccion


@login_required
def home(request):
    return render(request, "menuprincipal_wiki.html", {"cards": cards_data})

@login_required
def animales(request):
    return render(request, "Animales.html", {"animales": animales_data})

@login_required
def lugarestf(request):

    return render(
        request,
        "Lugarestf.html",
        {
            "pueblos": pueblos_data,
            "ubicaciones_especificas": ubicaciones_especificas_data,
            "ubicaciones_variadas": ubicaciones_variadas_data,
        },
    )

@login_required
def enemigos(request):
    return render(request, "Enemigos.html", {"enemigos": enemigos_data})

@login_required
def construcciones(request):
    construcciones = Construccion.objects.all()
    return render(request, "Construcciones.html", {"construcciones": construcciones})

@login_required
def flora(request):
    return render(request, "Flora.html", {"flora": flora_data})

@login_required
def armas(request):
    return render(request, "Armas.html", {"armas": armas_data})

@login_required
def consumibles(request):
    return render(request, "Consumibles.html", {"consumibles": consumibles_data})

@login_required
def historia(request):
    return render(
        request,
        "historia.html",
        {"historia_slider": historia_slider, "historia_texto": historia_texto},
    )

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
            return redirect("micuentatf")

        if form.is_valid():
            user = form.save()

            # Verifica si se quieren cambiar las contraseñas
            new_pass1 = request.POST.get("new_password1")
            new_pass2 = request.POST.get("new_password2")

            if new_pass1 or new_pass2:
                if new_pass1 != new_pass2:
                    messages.error(request, "Las contraseñas no coinciden.")
                    return redirect("micuentatf?edit=true&change_password=true")
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