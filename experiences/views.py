from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from home.decorators import admin_only

def experiences(request):
    experiences = Experience.objects.all()

    context = {"title": "Experiencia Laboral", "experiences": experiences}
    return render(request, 'experiences/experiences.html', context)


@login_required(login_url='loginPage')
def createExperience(request):
    experienceForm = CreateExperiencesForm()
    if request.method == 'POST':
        experienceForm = CreateExperiencesForm(request.POST, request.FILES)
        if experienceForm.is_valid():

            experienceForm.save()
            messages.success(request, 'La Experiencia fue creada')
            return redirect('experiences')

    context = {"title": "Crear Experiencia Laboral", "experienceForm": experienceForm}
    return render(request, 'experiences/createExperience.html', context)


@login_required(login_url='loginPage')
def editExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    experienceForm = CreateExperiencesForm(instance=experience)
    if request.method == 'POST':
        experienceForm = CreateExperiencesForm(request.POST, request.FILES, instance=experience)
        if experienceForm.is_valid:
            experienceForm.save()
            messages.success(request, 'La Experiencia fue Actualizada')
            return redirect('experiences')

    context = {"title": "Editar Experiencia", "experienceForm": experienceForm}
    return render(request, "experiences/editExperience.html", context)


@login_required(login_url='loginPage')
def deleteExperience(request, pk):
    experience = Experience.objects.get(id=pk)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'La Experiencia fue Eliminada')
        return redirect('experiences')

    context = {"title": "Eliminar Experiencia", 'item': experience}
    return render(request, 'experiences/deleteExperience.html', context)
