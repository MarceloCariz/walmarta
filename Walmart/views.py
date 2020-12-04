from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect


def inicio(request):
    return render(request, 'index.html')
