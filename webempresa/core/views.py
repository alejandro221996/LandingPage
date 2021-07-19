from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "core/home.html")
    # return HttpResponse("Inicio")


def about(request):
    # return HttpResponse("Historia")
    return render(request, "core/about.html")


def store(request):
    return render(request, "core/store.html")
    # return HttpResponse("Paquetes")
