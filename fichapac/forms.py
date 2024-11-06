from django import forms
from django.forms import ModelForm
from .models import Paciente, HistoriaClinica

class DateInput(forms.DateInput):
    input_type = 'date'


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'dni', 'domicilio', 'telefono', 'obrasocial', 'numafiliado', 'datecompleted', 'important']
        widgets = {
            'datecompleted' : DateInput()
        }
        labels = {
            'datecompleted' : 'Fecha de alta',
            'nombre' : 'Nombres',
            'telefono' : 'Teléfono',
            'obrasocial' : 'Obra social',
            'numafiliado' : 'Número de afiliado',
            'important' : 'Paciente importante',
        }

class HistoriaForm(ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'descripcion', 'diagnostico', 'datecompleted']
        widgets = {
            'datecompleted' : DateInput()
        }
        labels = {
            'datecompleted' : 'Fecha consulta',
            'descripcion' : 'Descripción',
            'diagnostico' : 'Diagnóstico',
        }
