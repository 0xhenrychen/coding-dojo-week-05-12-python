from django.shortcuts import render

from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)
    