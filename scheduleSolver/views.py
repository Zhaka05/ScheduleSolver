from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Application, Schedule
from .forms import AnketaForm
# Create your views here.

def index(request):
    # form data
    if request.method == "POST":
        ApplicationForm = Application()
        ApplicationForm.name = request.POST.get("name")
        ApplicationForm.last_name = request.POST.get("last_name")
        ApplicationForm.email = request.POST.get("email")
        ApplicationForm.phone = request.POST.get("phone")
        ApplicationForm.sports = request.POST.get("sports")
        ApplicationForm.year = request.POST.get("year")
        ApplicationForm.preferences.append(request.POST.get("preferred"))
        ApplicationForm.save()


    return render(request, 'form.html')

class Anketa(View):
    def get(self, request, *args, **kwargs):
        anketa = AnketaForm()

        return render(request, "example_form.html", {"anketa": anketa})
    
    def post(self, request, *args, **kwargs):
        print(request.POST.get("interests"))
        return HttpResponse(f"This is my classmate info\n {request}")