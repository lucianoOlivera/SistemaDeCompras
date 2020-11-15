import django.shortcuts
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from bases.views import SinPrivilegios
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv:categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases/login.html'


class CategoriaNew(SinPrivilegios, SuccessMessageMixin, generic.CreateView):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "categoria creada Sastifactoriamente"

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message = "categoria editada exitosamente"

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class CategotiaDel(SinPrivilegios, generic.DeleteView):
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')


class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = "inv/subcategoria:list.html"
    context_object_name = "obj"


class SubCategoriaNew(SinPrivilegios, generic.CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SinPrivilegios, generic.UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:categoria_list')

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


class SubCategotiaDel(SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')


class MarcaView(SinPrivilegios, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SinPrivilegios, generic.CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SinPrivilegios, generic.UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/')
@permission_required('inv.change_marca',login_url='bases:sin_privilegios')

def marca_inactiva (request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return django.shortcuts.redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca inactivada')
        return django.shortcuts.redirect("inv:marca_list")

    return django.shortcuts.render(request, template_name, contexto)


class UnidadMedidaView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/unidadMedida_list.html"
    context_object_name = "obj"


class UnidadMedidaNew(SinPrivilegios, generic.CreateView):
    model = UnidadMedida
    template_name = 'inv/unidadMedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadMedida_list')

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(SinPrivilegios, generic.UpdateView):
    model = UnidadMedida
    template_name = 'inv/unidadMedida_form.html'
    context_object_name = "obj"
    form_class = UnidadMedidaForm
    success_url = reverse_lazy('inv:unidadMedida_list')

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmedida',login_url='bases:sin_privilegios')
def UnidadMedida_inactiva (request, id):
    unidadMedida = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del2.html"

    if not unidadMedida:
        return django.shortcuts.redirect("inv:unidadMedida_list")

    if request.method == 'GET':
        contexto = {'obj': unidadMedida}

    if request.method == 'POST':
        unidadMedida.estado = False
        unidadMedida.save()
        return django.shortcuts.redirect("inv:unidadMedida_list")

    return django.shortcuts.render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"


class ProductoNew(SinPrivilegios, generic.CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')

    def form_valid (self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SinPrivilegios, generic.UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')

    def form_valid (self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto',login_url='bases:sin_privilegios')
def Producto_inactiva (request, id):
    producto = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not producto:
        return django.shortcuts.redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj': producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return django.shortcuts.redirect("inv:producto_list")

    return django.shortcuts.render(request, template_name, contexto)
