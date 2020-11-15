from django.urls import path
from .views import ProveedorNew,ProveedorEdit,ProveedorView , ProoveedorInactivar
urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', ProoveedorInactivar, name='proveedor_inactivar'),
    ]
