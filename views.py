from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from . models import FirstModel

# Create your views here.

class indexView(ListView):
    template_name = "ime2/ime2.html"
    model = FirstModel

    def home(request):
        return render(request, "ime2.html",{"name": "Navin"})

def add(request):
    val1= int(request.POST['num1'])
    val2= int( request.POST['num2'])
    res=val1+val2
    return render(request, 'result.html', {'result':res})