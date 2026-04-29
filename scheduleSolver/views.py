from django.shortcuts import render
from django.http import HttpResponse
from .models import Application
# Create your views here.

def index(request):
    selected_preferences = ["WE", "EM", "LN"]
    form = Application(
        name="Zhansen",
        year="VL",
        last_name="Shingis",
        email="<EMAIL>",
        phone="3093915377",
        sports="Sports",
        preferences=selected_preferences,
    )
    form.save()

    for obj in Application.objects.all():
        print(obj.name)

    return HttpResponse(form.name)