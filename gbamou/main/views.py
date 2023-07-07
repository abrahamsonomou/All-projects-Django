from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    info= Info.objects.order_by('-updated')[:1]
    competences = Competences.objects.order_by('-updated')
    competencesup = CompetenceSuplementaire.objects.order_by('-updated')
    services = Service.objects.all()
    portfolios = Portfolio.objects.filter(status=True)[:8]
    educations = Education.objects.order_by('-updated')
    experiences = Experience.objects.order_by('-updated')
    formations = FormationAttestee.objects.order_by('-updated')
    certs = Certification.objects.all()
    temoignages = Temoignage.objects.filter(status=True)
    sliders = Slider.objects.filter(status=True)

    context={
            'portfolios':portfolios,
            'temoignages':temoignages,
            'services':services,
            'competences':competences,
            'competencesup':competencesup,
            'infos':info,
            'sliders':sliders,
            'educations':educations,
            'experiences':experiences,
            'formations':formations,
            'certs':certs,
            }
    return render(request,"client/index.html",context)
