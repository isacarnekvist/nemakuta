from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frontpage(request):
    ctx = {
        'home_active': True,
    }
    return render(request, 'web/frontpage.html', context=ctx)


def rooms(request):
    ctx = {
        'rooms_active': True,
    }
    return render(request, 'web/rooms.html', context=ctx)
