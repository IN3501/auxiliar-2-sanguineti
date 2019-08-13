from django.shortcuts import render


# Create your views here.

def cuerpo_docente(request):
    return render(request, 'miapp/cuerpo_docente.html')


def index(request):
    return render(request, 'miapp/index.html')


def pestaña(request):
    return render(request, 'miapp/pestaña.html')
