from django.shortcuts import render, redirect
from .models import Coche



#jorvegap.95@gmail.com


def Carros(request):
    if request.method == 'GET':
        listaCarros = Coche.objects.all()
        return render(request, 'carros.html', {'carros':listaCarros})
    

def formCar(request):
    if request.method == 'GET':
        return render(request, 'crearCarro.html')


def CarroId(request, Id):
    if request.method == 'GET':
        car = Coche.objects.get(ID=Id)
        return render(request, 'editarCarro.html', {'carro':car})

def CrearCarro(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        color = request.POST['color']
        modelo = request.POST['modelo']
        Carro = Coche.objects.create(marca=marca, color=color, modelo=modelo)
        return redirect('home')
    
def ActualizarCarro(request, Id):
    if request.method == 'POST':
        marca = request.POST['marca']
        color = request.POST['color']
        modelo = request.POST['modelo']
        
        Carro = Coche.objects.get(ID=Id)
        
        Carro.marca = marca
        Carro.color = color
        Carro.modelo = modelo
        Carro.save()
        return redirect('home')


def BorrarCarro(request,Id):
    if request.method == 'GET':
        Carro=Coche.objects.get(ID=Id)
        Carro.delete()
        return redirect('home')
    
