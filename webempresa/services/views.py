from django.shortcuts import render
from .models import services as sv

# Create your views here.


def services(request):
    # return HttpResponse("Servicios")
    servicios = sv.objects.all()
    return render(request, "services/services.html", {'services': servicios})
