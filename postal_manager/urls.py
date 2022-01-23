from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("entrega-objetos/", Entrega_objetos.as_view(), name="entrega_objetos"),
    path("cadastro-simples/", Cad_obj_simples.as_view(), name="cad_obj_simp"),
    path("cadastro-qualificados/", Cad_obj_qual.as_view(), name="cad_obj_qual"),
    path("tipos-postais/", Tipos_postais.as_view(), name="tipos_postais"),
    path("objetos-vencidos/", Obj_vencidos.as_view(), name="obj_vencidos"),
    path("entrega-objetos/<pk>/entregar", Entrega_objetoView.as_view()),
]
