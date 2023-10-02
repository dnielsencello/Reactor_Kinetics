from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Reactors

# Create your views here.
def index(request):
    reactors = Reactors.objects
    return render(request, 'reactors/index.html',{'reactors':reactors})

def details(request, reactor_id):
    reactor_detail = get_object_or_404(Reactors, pk = reactor_id)
    return render(request, 'reactors/detail.html', {'reactor': reactor_detail})
