from django.contrib import admin
from .models import Paciente, HistoriaClinica

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
  readonly_fields = ('created', )

admin.site.register(Paciente, PacienteAdmin)


class HistoriaClinicaAdmin(admin.ModelAdmin):
  model = HistoriaClinica

admin.site.register(HistoriaClinica)





