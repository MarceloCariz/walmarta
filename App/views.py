from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Nombre
from .forms import NombreForm
from django.http import HttpResponse

# Create your views here.


def CrearNombre(request):
    if request.method == 'POST':
        nombre_form = NombreForm(request.POST)
        if nombre_form.is_valid():
            nombre_form.save()
            return redirect('nombre:nombre')
    else:
        nombre_form = NombreForm()
    return render(request, 'index.html', {'nombre_form': nombre_form})


def ListarNombre(request):
    nombres = Nombre.objects.all()
    return render(request, 'listarNombre.html', {'nombres': nombres})


def editarNombre(request, id):
    nombre_form = None
    error = None
    try:
        nombres = Nombre.objects.get(id=id)
        if request.method == 'GET':
            nombre_form = NombreForm(instance=nombres)
        else:
            nombre_form = NombreForm(request.POST, instance=nombres)
            if nombre_form.is_valid():
                nombre_form.save()
                return redirect('listar:listar')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'index.html', {'nombre_form': nombre_form, 'error': error})


def eliminarNombre(request, id):
    nombres = Nombre.objects.get(id=id)
    if request.method == 'POST':
        nombres.delete()
        return redirect('listar:listar')
    return render(request, 'eliminar_nombre.html', {'nombres': nombres})
