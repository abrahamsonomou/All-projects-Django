from django.shortcuts import render
from .models import *

# Create your views here.
def formation(request):

    list_cours=Cours.objects.all()
    nos_formations=Formation.objects.all()
    recent_cours=Cours.objects.order_by('-plublish')[:5]

    context={
            'list_cours':list_cours,
            'nos_formations':nos_formations,
            'recent_cours':recent_cours,
            }
    return render(request,"pages/classroom.html",context)