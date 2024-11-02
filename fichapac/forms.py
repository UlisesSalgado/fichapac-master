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

class HistoriaForm(ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'descripcion', 'diagnostico', 'datecompleted']
        widgets = {
            'datecompleted' : DateInput()
        }