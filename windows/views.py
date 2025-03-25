import random

from django.shortcuts import render

from home.static_data import *


def index(request):
    context = {
        'SEO_title': 'Надежные ПВХ окна от производителя - Проф-Лайн',
        'sliders': WINDOWS_SLIDERS[0],
        'about_description': WINDOWS_ABOUT_DESCRIPTION,
        'about_windows': WINDOWS_ABOUT_WINDOWS,
        'portfolio':  random.sample(WINDOWS_PORTFOLIO, 12),
        'services': WINDOWS_SERVICES,
    }

    return render(request, 'windows/index.html', context)
