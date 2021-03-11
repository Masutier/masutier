from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from home.decorators import admin_only

def skills(request):
    skills = Skill.objects.all()

    context = {"title": "Skills", "skills": skills}
    return render(request, "skills/skills.html", context)


@login_required(login_url='loginPage')
def createSkill(request):
    skillForm = CreateSkillForm()

    if request.method == 'POST':
        skillForm = CreateSkillForm(request.POST, request.FILES)
        if skillForm.is_valid():

            skillForm.save()
            messages.success(request, 'El Skill fue creado')
            return redirect('skills')

    context = {"title": "Crear Skill", "skillForm": skillForm}
    return render(request, "skills/createSkill.html", context)


@login_required(login_url='loginPage')
def editSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    skillForm = CreateSkillForm(instance=skill)
    if request.method == 'POST':
        skillForm = CreateSkillForm(request.POST, request.FILES, instance=skill)
        if skillForm.is_valid:
            skillForm.save()
            messages.success(request, 'El Skill fue Actualizado')
            return redirect('skills')

    context = {"title": "Editar Skill", "skillForm": skillForm}
    return render(request, "skills/editSkill.html", context)


@login_required(login_url='loginPage')
def deleteSkill(request, pk):
    skill = Skill.objects.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'El Skill fue Eliminado')
        return redirect('skills')

    context = {"title": "Eliminar Skill", 'item': skill}
    return render(request, 'skills/deleteSkill.html', context)
