from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  edad = models.IntegerField(null=True, blank=True)
  dni = models.IntegerField(unique=True)
  domicilio = models.CharField(max_length=100, null=True, blank=True)
  telefono = models.BigIntegerField(null=True, blank=True)
  obrasocial = models.CharField(max_length=100)
  numafiliado = models.BigIntegerField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre +' '+ self.apellido + ' Dr: ' + self.user.username


  
class HistoriaClinica(models.Model):
  paciente = models.ForeignKey(Paciente, related_name='diagnosticos', on_delete=models.CASCADE)
  descripcion = models.CharField(max_length=100, null=True, blank=True)
  diagnostico = models.TextField(max_length=1000)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return f"Paciente: {self.paciente} by {self.user}"



