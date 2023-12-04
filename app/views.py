from django.shortcuts import render
from .forms import Alumno

# Create your views here.


def registrar(request):
    if request.method == "POST":
        # crear objeto de la clase alumno
        form = Alumno(request.POST)
        if form.is_valid():
            # recuperar datos del la pagina html y asignar valores a variables
            código = form.cleaned_data["código"]
            nombre = form.cleaned_data["nombre"]
            curso = form.cleaned_data["curso"]
            parcial = form.cleaned_data["parcial"]
            practica = form.cleaned_data["practica"]
            final = form.cleaned_data["final"]
        
            promedio = (parcial+practica+2*final)/4
            if promedio >= 14:
                estado = "Aprobado"
            elif promedio >= 10 and promedio < 14:
                estado = "Sustitutorio"
            else:
                estado = "Desaprobado"
            contexto = {'código': código, 'nombre': nombre, 'curso': curso,
                        'parcial': parcial, 'practica': practica, 'final': final, 'promedio': promedio, 'estado': estado}
            return render(request, 'app/boleta.html', contexto)
    else:
        # crear objeto de la clase alumno
        form = Alumno()
    contexto = {'form': form}
    return render(request, 'app/registrar.html', contexto)
