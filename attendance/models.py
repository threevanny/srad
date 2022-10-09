from django.db import models

# Create your models here.

# class Teacher(models.Model):
#   user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
#   phone = models.CharField(max_length=64, blank=True)
#   address = models.CharField(max_length=64, blank=True)
#   rank = models.CharField(max_length=16) # Categorias: Auxialiar, Asistente, Asociado, Titular

#   def __str__(self):
#     return self.user.username

class Class(models.Model):
  plan = models.IntegerField()                    # plan
  semester = models.IntegerField()                # semestre
  code = models.CharField(max_length=128)         # codigo
  cluster = models.IntegerField()                 # Grupo
  name = models.CharField(max_length=128)         # Nombre
  campus = models.CharField(max_length=128)       # Sede
  time = models.CharField(max_length=128)         # Jornada
  intensity = models.IntegerField()               # intensidad
  classroom = models.CharField(max_length=128)    # Salón  
  day = models.CharField(max_length=16)           # Dia
  start_time = models.TimeField()                 # Hora de inicio
  end_time = models.TimeField()                   # Hora de finalización
  is_checked = models.BooleanField(default=False)
  checked_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  teacher = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return str(self.plan) + ' - ' +  self.name
  
class Report(models.Model):
  students = models.IntegerField()
  class_date = models.DateField()
  impact = models.CharField(max_length=128)
  description = models.TextField(max_length=1024)
  created_at = models.DateTimeField(auto_now_add=True)
  # teahcher


  def __str__(self):
    return self.created_at