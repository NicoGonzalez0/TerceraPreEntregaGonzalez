from django.shortcuts import render, redirect
from .forms import FormularioDatos, FormularioBusqueda
from .models import Clase1, Clase2, Clase3

def insertar_datos(request):
    if request.method == 'POST':
        form = FormularioDatos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insertar_datos')
    else:
        form = FormularioDatos()
    
    return render(request, 'insertar_datos.html', {'form': form})

def buscar_datos(request):
    if request.method == 'POST':
        form = FormularioBusqueda(request.POST)
        if form.is_valid():
            datos = form.cleaned_data['busqueda']
            resultados = Clase1.objects.filter(campo1__icontains=datos) | \
                         Clase2.objects.filter(campo3__icontains=datos) | \
                         Clase3.objects.filter(campo5__icontains=datos)
            return render(request, 'buscar_datos.html', {'form': form, 'resultados': resultados})
    else:
        form = FormularioBusqueda()
    
    return render(request, 'buscar_datos.html', {'form': form})