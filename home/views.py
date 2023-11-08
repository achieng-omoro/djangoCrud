from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import driver, Slider
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html', {'navbar': 'home'})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def drive(request):
    return render(request, 'driver.html', {'navbar': 'driver'})


def hire(request):
    paginate = Paginator(driver.objects.all(), 4)
    page = request.GET.get('page')
    data = paginate.get_page(page)

    # data = driver.objects.all()
    return render(request, 'hire.html', {'navbar': 'hire', 'data': data})


def delete(request, id):
    dbdrivers = driver.objects.get(id=id)
    dbdrivers.delete()
    messages.success(request, 'Record deleted successfully')
    return redirect("/hire")


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        licence = request.POST.get('licence')
        image = request.FILES['image']

        # if len(request.FILES)!=0:

        details = driver(name=name, email=email, phone=phone, licence=licence, image=image)
        details.save()
        messages.success(request, 'Record added successfully')
        return redirect("/hire")

    return redirect("/hire")


def edit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        licence = request.POST.get('licence')
        image = request.FILES['image']

        driverd = driver.objects.get(id=id)

        driverd.name = name
        driverd.email = email
        driverd.phone = phone
        driverd.licence = licence
        driverd.image = image
        driverd.save()
        messages.success(request, 'Record updated successfully')

        return redirect("/hire")

    drivers = driver.objects.get(id=id)
    return render(request, 'edit.html', {'driver': drivers})


def slider(request):
    slides = Slider.objects.all()
    return render(request, 'slider.html', {'navbar': 'slider', 'slides': slides})


# def hire(request):
#     data = driver.objects.all()
#     return render(request, 'hire.html', {'navbar': 'hire', 'data':data})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query:
            drivers = driver.objects.filter(name__contains=query)
            return render(request, 'search.html', {'navbar': 'search', 'data': drivers})
    return render(request, 'search.html')
