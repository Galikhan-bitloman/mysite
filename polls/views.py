from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = "Galik"
    return render(request, "home.html", {"name": name})

# Create your views here.
