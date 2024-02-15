
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email =models.EmailField(max_length = 254)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
   
    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Registers"
        ordering = ('id',)

    
    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
   
    class Meta:
        verbose_name = "Login"
        verbose_name_plural = "Logins"
        ordering = ('id',)

    
    def __str__(self):
        return self.username