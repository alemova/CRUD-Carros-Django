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
        car = Coche.objects.get(Id)
        return render(request, 'editarCarro.html', {'carro':car})

def CrearCarro(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        color = request.POST['color']
        modelo = request.POST['modelo']
        Carro = Coche.objects.create(marca=marca, color=color, modelo=modelo)
        return redirect('carros')
    
def ActualizarCarro(request):
    if request.method == 'POST':
        id = request.POST['id']
        marca = request.POST['marca']
        color = request.POST['color']
        modelo = request.POST['modelo']
        
        Carro = Coche.objects.get(id=id)
        
        Carro.marca = marca
        Carro.color = color
        Carro.modelo = modelo
        Carro.save()
        return redirect('carros')


def BorrarCarro(request):
    if request.method == 'POST':
        id  = request.POST['id']
        Carro=Coche.objects.get(id=id)
        Carro.delete()
        return redirect('carros')
    
