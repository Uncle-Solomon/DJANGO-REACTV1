from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "hello_webpack.html")
