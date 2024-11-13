from django.template import loader
from django.http import HttpResponse
from .models import Car
from django.shortcuts import render, redirect
from .forms import CarForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def cars(request):
    my_cars = Car.objects.all().values()
    template = loader.get_template('all_cars.html')
    context = {
        'my_cars': my_cars,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my_cars = Car.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_cars': my_cars
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'cars': ['Sedan', 'Coupe', 'SUV']
    }
    return HttpResponse(template.render(context, request))

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars')  # Redirect to the car list after saving
    else:
        form = CarForm()
    
    context = {
        'form': form
    }
    return render(request, 'create_car.html', context)

def edit_car(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars')  # Redirect to the car list after saving
    else:
        form = CarForm(instance=car)

    context = {
        'form': form,
        'car': car
    }
    return render(request, 'edit_car.html', context)

def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car.delete()
        return HttpResponseRedirect(reverse('cars'))  # Redirect to the car list after deletion
    return render(request, 'confirm_delete.html', {'car': car})
