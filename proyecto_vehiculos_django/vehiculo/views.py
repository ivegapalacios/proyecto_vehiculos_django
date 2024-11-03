from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import VehiculoForm, UserRegistrationForm
from .models import Vehiculo

# Create your views here.
@login_required
def index(request):
    return render(request, 'vehiculo/index.html')

class CustomLoginView(LoginView):
    template_name = 'vehiculo/registration/login.html'

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all() #obtiene todos los vehiculos de la base de datos
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            #Asignar el permiso de visualizar catálogo
            permission = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permission)
            login(request, user)  #Iniciar sesión automáticamente después del registro
            return redirect('index')  #Redirigir a una página después del registro
    else:
        form = UserRegistrationForm()
    return render(request, 'vehiculo/registration/register.html', {'form': form})

@login_required
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vehículo agregado correctamente!')
            form = VehiculoForm()  #nueva instancia para limpiar los campos
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})