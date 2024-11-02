from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Paciente, HistoriaClinica

from .forms import PacienteForm, HistoriaForm

# Create your views here.

# Crear usuario, inicio sesion, cerrar sesion.

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('pacientes')
            except IntegrityError:
                return render(request, 'registrarse.html', {"form": UserCreationForm, "error": "El usuario ya existe."})

        return render(request, 'registrarse.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})
    
def home(request):
    return render(request, 'home.html')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar_sesion.html', {"form": AuthenticationForm, "error": "Usuario y/o contraseña incorrectas."})

        login(request, user)
        return redirect('pacientes')


# Creacion de pacientes, añadir, eliminar, etc.

#@login_required
#def pacientes(request):
    pacientes = Paciente.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'pacientes.html', {"pacientes": pacientes})

#@login_required
#def pacientes_añadidos(request):
    pacientes = Paciente.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'pacientes.html', {"pacientes": pacientes})

@login_required
def pacientes(request):
    pacientes = Paciente.objects.filter(user=request.user).order_by('apellido', '-dni')
    return render(request, 'pacientes.html', {"pacientes": pacientes})

@login_required
def añadir_paciente(request):
    if request.method == "GET":
        return render(request, 'añadir_paciente.html', {"form": PacienteForm})
    else:
        try:
            form = PacienteForm(request.POST)
            new_pac = form.save(commit=False)
            new_pac.user = request.user
            new_pac.save()
            return redirect('pacientes')
        except ValueError:
            return render(request, 'añadir_paciente.html', {"form": PacienteForm, "error": "Error al añadir paciente."})
        
def paciente_detail(request, paciente_id):
    if request.method == 'GET':
        paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
        form = PacienteForm(instance=paciente)
        return render(request, 'paciente_detail.html', {'paciente': paciente, 'form': form})
    else:
        try:
            paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
            form = PacienteForm(request.POST, instance=paciente)
            form.save()
            return redirect('pacientes')
        except ValueError:
            return render(request, 'paciente_detail.html', {'paciente': paciente, 'form': form, 'error': 'Error actualizando paciente.'})
        
@login_required
def delete_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id, user=request.user)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')
        

# Creacion de historias clinicas, añadir, eliminar, etc.

@login_required
def historias(request):
    historias = HistoriaClinica.objects.filter(user=request.user).order_by('-datecompleted')
    return render(request, 'historias.html', {"historias": historias})

"""@login_required
def consultas_añadidas(request):
    historias = HistoriaClinica.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'historias.html', {"historias": historias})"""

@login_required
def añadir_consulta(request):
    if request.method == "GET":
        return render(request, 'añadir_consulta.html', {"form": HistoriaForm})
    else:
        try:
            form = HistoriaForm(request.POST)
            new_his = form.save(commit=False)
            new_his.user = request.user
            new_his.save()
            return redirect('historias')
        except ValueError:
            return render(request, 'añadir_consulta.html', {"form": HistoriaForm, "error": "Error al crear consulta."})

@login_required
def historia_detail(request, historia_id):
    if request.method == 'GET':
        historia = get_object_or_404(HistoriaClinica, pk=historia_id, user=request.user)
        form = HistoriaForm(instance=historia)
        return render(request, 'historia_detail.html', {'historia': historia, 'form': form})
    else:
        try:
            historia = get_object_or_404(HistoriaClinica, pk=historia_id, user=request.user)
            form = HistoriaForm(request.POST, instance=historia)
            form.save()
            return redirect('historias')
        except ValueError:
            return render(request, 'historia_detail.html', {'historia': historia, 'form': form, 'error': 'Error actualizando historia clínica.'})
        

@login_required
def delete_historia(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, pk=historia_id, user=request.user)
    if request.method == 'POST':
        historia.delete()
        return redirect('historias')

@login_required
def filtrar_historias(request):
    dni = request.GET.get('dni', '')
    if dni:
        historias = HistoriaClinica.objects.filter(user=request.user, paciente__dni__icontains=dni)
    else: 
        historias = HistoriaClinica.objects.filter(user=request.user)
    
    return render(request, 'historias.html', {'historias': historias})

