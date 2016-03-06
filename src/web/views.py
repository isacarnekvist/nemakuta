from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

from .models import House


def frontpage(request):
    ctx = {
        'home_active': True,
    }
    return render(request, 'web/frontpage.html', context=ctx)


def rooms(request):
    houses = House.objects.all()
    for house in houses:
        house.img_path = static('img/rooms/{}'.format(house.img_path))
    ctx = {
        'rooms_active': True,
        'houses': houses,
    }
    return render(request, 'web/rooms.html', context=ctx)
