from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frontpage(request):
    return render(request, 'web/frontpage.html')
