from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategotiaDel, SubCategoriaView ,\
    SubCategoriaNew ,SubCategoriaEdit,SubCategotiaDel,MarcaView,MarcaNew,MarcaEdit , marca_inactiva, UnidadMedidaNew, UnidadMedidaEdit,UnidadMedida_inactiva ,\
    UnidadMedidaView , ProductoView , ProductoNew , ProductoEdit , Producto_inactiva

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategotiaDel.as_view(), name='categoria_del'),

    path('subcategoria/', SubCategoriaView.as_view() , name='subcategoria_list'),
    path('subcategoria/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategotiaDel.as_view(), name='subcategoria_del'),

    path('marca/', MarcaView.as_view() , name='marca_list'),
    path('marca/new', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>', marca_inactiva, name='marca_inactiva'),

    path('unidadDeMedida/', UnidadMedidaView.as_view() , name='unidadMedida_list'),
    path('unidadDeMedida/new', UnidadMedidaNew.as_view(), name='unidadMedida_new'),
    path('unidadDeMedida/edit/<int:pk>', UnidadMedidaEdit.as_view(), name='unidadMedida_edit'),
    path('unidadDeMedida/inactivar/<int:id>', UnidadMedida_inactiva, name='unidadMedida_inactiva'),

    path('producto/', ProductoView.as_view(), name='producto_list'),
    path('producto/new', ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:id>', Producto_inactiva, name='producto_inactiva'),

]
