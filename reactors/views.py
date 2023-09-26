from django.shortcuts import render

from django.http import HttpResponse

from .models import Reactors

# Create your views here.
def index(request):
    reactors = Reactors.objects
    return render(request, 'reactors/index.html',{'reactors':reactors})
