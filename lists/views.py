from django.shortcuts import render
import django.http as django_http

# Create your views here.


def home_page(request: django_http.HttpRequest) -> django_http.HttpResponse:
    print(f"post : {request.POST}")
    print(f'new_item_text : {request.POST.get("item_text", "")}')
    return render(
        request, "home.html", {"new_item_text": request.POST.get("item_text", "")}
    )
