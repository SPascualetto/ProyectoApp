from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    Titulo=models.CharField(max_length=255)
    Carrera = models.CharField(max_length=255)
    Nombre=models.ForeignKey(User, on_delete=models.CASCADE)
    Cuerpo = models.TextField()
    post_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Titulo  + ' | ' + str(self.Nombre)
    
    def get_absolute_url(self):
        return reverse('home')


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    def _str_(self):
        return f"{self.user} - {self.imagen}"
    
    