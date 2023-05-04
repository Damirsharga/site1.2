from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name")
    message = request.GET.get("message")
    return HttpResponse(f"<h2>Hello {name}! <br> {message}!</h2>")