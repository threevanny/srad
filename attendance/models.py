from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Teacher(models.Model):
#   #   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#   RANK_CHOICES = [
#     ('Auxiliar', 'Auxiliar'),
#     ('Asistente', 'Asistente'),
#     ('Asociado', 'Asociado'),
#     ('Titular', 'Titular'),

#   ]

#   # Categorias: Auxialiar, Asistente, Asociado, Titular
#   rank = models.CharField(max_length=100, null=True)

#   def __str__(self):
#     return self.name

# class Class(models.Model):
#   def __str__(self):
#     return self.name