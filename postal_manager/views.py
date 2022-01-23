from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import *


class Index(TemplateView):
    template_name = "postal_manager/index.html"


class Entrega_objetos(ListView):
    model = Objetos_db
    template_name = "postal_manager/entrega_objetos.html"


class Cad_obj_simples(CreateView):
    model = Objetos_db
    fields = ["destinatario", "classe_obj"]
    template_name = "postal_manager/cadastrar_obj_simples.html"
    success_url = reverse_lazy("cad_obj_simp")


class Cad_obj_qual(CreateView):
    model = Objetos_db
    fields = ["destinatario", "classe_obj"]
    template_name = "postal_manager/cadastrar_obj_qual.html"
    success_url = reverse_lazy("cad_obj_qual")


class Tipos_postais(CreateView):
    model = Tipos_postais_db
    fields = ["classe_obj", "sigla_obj"]
    template_name = "postal_manager/tipos_postais.html"
    success_url = reverse_lazy("cad_obj_simp")


class Obj_vencidos(ListView):
    model = Objetos_db
    template_name = "postal_manager/obj_vencidos.html"


class Entrega_objetoView(DeleteView):
    model = Objetos_db
    success_url = reverse_lazy("entrega_objetos")


class Devolve_objetoView(DeleteView):
    model = Objetos_db
    success_url = reverse_lazy("obj_vencidos")
