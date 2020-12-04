from django.urls import path
from .views import CrearNombre, ListarNombre, editarNombre, eliminarNombre

urlpatterns = [

    path('', CrearNombre, name='nombre'),
    path('listar/', ListarNombre, name='listar'),
    path('editar_nombre/<int:id>', editarNombre, name='editar_nombre'),
    path('eliminar_nombre/<int:id>', eliminarNombre, name='eliminar_nombre'),


]
