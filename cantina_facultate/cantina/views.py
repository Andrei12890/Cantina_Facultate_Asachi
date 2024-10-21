from django.shortcuts import render
from cantina.models import Produs


def prima_pagina(request):
    return render(request, 'cantina/prima_pagina.html')


def meniu(request):
    produse = [
        {'denumire': 'Ciorba rădăuțeană','pret': 3.5},
        {'denumire': 'Ciorbă de perișoare', 'pret': 5.19},
        {'denumire': 'Cascaval pane', 'pret': 4.55},
        {'denumire': 'Chiftele cu carne și sos', 'pret': 6.5},
        {'denumire': 'Grătar din piept de pui', 'pret': 8},
        {'denumire': 'Mici cu muștar', 'pret': 2},
        {'denumire': 'Tochitură moldovenească', 'pret': 10},
        {'denumire': 'Pâine felie', 'pret': 0.25},
        {'denumire': 'Mămăligă', 'pret': 0.25},
    ]
    return render(request, 'cantina/meniu.html', {'produse': produse})


def contact(request):
    return render(request, 'cantina/contact.html')
