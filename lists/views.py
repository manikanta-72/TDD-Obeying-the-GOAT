from django.shortcuts import render
import django.http as django_http

# Create your views here.


def home_page(request: django_http.HttpRequest) -> django_http.HttpResponse:
    return django_http.HttpResponse("<html><title>To-Do Lists</title></html>")
