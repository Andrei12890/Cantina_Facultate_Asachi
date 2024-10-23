from django.shortcuts import render
from cantina.models import Produs


def prima_pagina(request):
    return render(request, 'cantina/prima_pagina.html')


def meniu(request):
    produse = Produs.objects.all()
    return render(request, 'cantina/meniu.html', {'produse': produse})


def contact(request):
    return render(request, 'cantina/contact.html')
