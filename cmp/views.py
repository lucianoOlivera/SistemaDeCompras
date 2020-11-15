from django.urls import reverse_lazy
from django.views import generic
from bases.views import SinPrivilegios
from .forms import ProveedorForm
from .models import Proveedor
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

class ProveedorView(SinPrivilegios, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"


class ProveedorNew(SinPrivilegios, generic.CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProveedorEdit(SinPrivilegios, generic.UpdateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'base:login'

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('cmp.change_proovedor',login_url='bases:sin_privilegios')
def ProoveedorInactivar (request, id):
    template_name = 'cmp/inactivar_prv.html'
    ctx = {}
    prv = Proveedor.objects.filter(pk=id).first()
    if not prv:
        return HttpResponse('proveedor no existe ' + str(id))
    if request.method == 'GET':
        ctx = {'obj': prv}
    if request.method == 'POST':
        prv.estado=False
        prv.save()
        ctx = {'obj': 'ok'}
        return HttpResponse('proveedor inactivado')
    return render(request, template_name, ctx)


