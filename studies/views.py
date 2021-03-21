from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from home.decorators import admin_only

def studies(request):
    univ = Studie.objects.filter(kind='University').order_by('-yearEnd')
    tech = Studie.objects.filter(kind='Technical').order_by('-yearEnd')
    wshop = Studie.objects.filter(kind='WorkShop').order_by('-yearEnd')
    myself = Studie.objects.filter(kind='Self').order_by('-yearEnd')
    other = Studie.objects.filter(kind='Other').order_by('-yearEnd')

    context = {"title": "Education", "univ": univ, "tech": tech, "wshop": wshop, "myself": myself, "other": other}
    return render(request, 'studies/studies.html', context)


@login_required(login_url='loginPage')
def createStudie(request):
    studieForm = CreateStudieForm()
    if request.method == 'POST':
        studieForm = CreateStudieForm(request.POST, request.FILES)
        if studieForm.is_valid():

            studieForm.save()
            messages.success(request, 'The course was created successful')
            return redirect('studies')

    context = {"title": "Create Education", "studieForm": studieForm}
    return render(request, 'studies/createStudie.html', context)


@login_required(login_url='loginPage')
def editStudie(request, pk):
    study = Studie.objects.get(id=pk)
    studieForm = CreateStudieForm(instance=study)
    if request.method == 'POST':
        studieForm = CreateStudieForm(request.POST, request.FILES, instance=study)
        if studieForm.is_valid:
            studieForm.save()
            messages.success(request, 'The course was Updated successful')
            return redirect('studies')

    context = {"title": "Update Education", "studieForm": studieForm}
    return render(request, "studies/editStudie.html", context)


@login_required(login_url='loginPage')
def deleteStudie(request, pk):
    study = Studie.objects.get(id=pk)
    if request.method == 'POST':
        study.delete()
        messages.success(request, 'The course was Deleted')
        return redirect('studies')

    context = {"title": "Delete Education", 'item': study}
    return render(request, 'studies/deleteStudie.html', context)
