from django.urls import path
from . import views
from .views import (
    home,
    animales,
    lugarestf,
    enemigos,
    construcciones,
    flora,
    armas,
    consumibles,
    historia,
    forowiki,
    inicio_sesion_wiki,
    micuentatf,
    recuperarcontra,
    registrase,
    cerrar_sesion,
    eliminar_construccion,
    editar_construccion,
    clima_chile,
)

urlpatterns = [
    path("", home, name="home"),
    path("animales", animales, name="animales"),
    path("lugarestf", lugarestf, name="lugarestf"),
    path("enemigos", enemigos, name="enemigos"),
    path("construcciones", construcciones, name="construcciones"),
    path("flora", flora, name="flora"),
    path("armas", armas, name="armas"),
    path("consumibles", consumibles, name="consumibles"),
    path("historia", historia, name="historia"),
    path("forowiki", forowiki, name="forowiki"),
    path("inicio_sesion_wiki", inicio_sesion_wiki, name="inicio_sesion_wiki"),
    path('micuentatf', views.micuentatf, name='micuentatf'),

    path("recuperarcontra", recuperarcontra, name="recuperarcontra"),
    path("registrase", registrase, name="registrase"),
    path("logout", cerrar_sesion, name="logout"),
    path('construcciones/eliminar/<int:pk>/', eliminar_construccion, name='eliminar_construccion'),
    path('construccion/<int:id>/editar/', editar_construccion, name='editar_construccion'),
    path("clima/", clima_chile, name="clima_chile"),
    path('animal/<int:id>/editar/', views.editar_animal, name='editar_animal'),
    path('pueblo/<int:id>/editar/', views.editar_pueblo, name='editar_pueblo'),
    path('ubicacion_especifica/<int:id>/editar/', views.editar_ubicacion_especifica, name='editar_ubicacion_especifica'),
    path('ubicacion_variada/<int:id>/editar/', views.editar_ubicacion_variada, name='editar_ubicacion_variada'),
    path('enemigo/<int:id>/editar/', views.editar_enemigo, name='editar_enemigo'),
    path('planta/<int:id>/editar/', views.editar_planta, name='editar_planta'),
    path('arma/<int:id>/editar/', views.editar_arma, name='editar_arma'),
    path('consumible/<int:id>/editar/', views.editar_consumible, name='editar_consumible'),
    path('historia/<int:id>/editar/', views.editar_historia, name='editar_historia'),





]
