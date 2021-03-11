from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from home.decorators import admin_only

def studies(request):
    univ = Studie.objects.filter(kind='University')
    tech = Studie.objects.filter(kind='Technical')
    other = Studie.objects.filter(kind='Other')

    context = {"title": "Studies", "univ": univ, "tech": tech, "other": other}
    return render(request, 'studies/studies.html', context)


@login_required(login_url='loginPage')
def createStudie(request):
    studieForm = CreateStudieForm()
    if request.method == 'POST':
        studieForm = CreateStudieForm(request.POST, request.FILES)
        if studieForm.is_valid():

            studieForm.save()
            messages.success(request, 'El Curso fue creado')
            return redirect('studies')

    context = {"title": "Create Studies", "studieForm": studieForm}
    return render(request, 'studies/createStudie.html', context)


@login_required(login_url='loginPage')
def editStudie(request, pk):
    study = Studie.objects.get(id=pk)
    studieForm = CreateStudieForm(instance=study)
    if request.method == 'POST':
        studieForm = CreateStudieForm(request.POST, request.FILES, instance=study)
        if studieForm.is_valid:
            studieForm.save()
            messages.success(request, 'El Estudio fue Actualizado')
            return redirect('studies')

    context = {"title": "Editar Estudio", "studieForm": studieForm}
    return render(request, "studies/editStudie.html", context)


@login_required(login_url='loginPage')
def deleteStudie(request, pk):
    study = Studie.objects.get(id=pk)
    if request.method == 'POST':
        study.delete()
        messages.success(request, 'El Estudio fue Eliminado')
        return redirect('studies')

    context = {"title": "Eliminar Estudio", 'item': study}
    return render(request, 'studies/deleteStudie.html', context)
