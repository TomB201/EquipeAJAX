from django.http import JsonResponse
from django.shortcuts import render, redirect
from projet1WEBA.models import *
from templates.forms import *

def index(request):
    return render(request, "index.html")

def equipe(request):
    equipes = Equipe.objects.all()
    content = {"equipes": equipes}
    return render(request, "show_equipes.html", content)


def add_equipe(request):
    if request.method == "POST":
        form = Form_addequipe(request.POST)
        if form.is_valid():
            new_equipe = Equipe()
            new_equipe.nom = form.cleaned_data["nom"]
            new_equipe.pays = form.cleaned_data["pays"]
            new_equipe.save()
            return redirect("equipes")
    else:
        form = Form_addequipe()
        content = {"form": form}
        return render(request, "add_equipes.html", content)

def equipe_details(request, id):
    equipe = Equipe.objects.get(id=id)
    details = {
        "nom": equipe.nom,
        "pays": equipe.pays,
        "ville": equipe.ville,
        "couleurs": equipe.couleurs,
    }
    return JsonResponse(details)