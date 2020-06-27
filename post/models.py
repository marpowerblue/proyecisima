from django.db import models


class User (models.Model):
    email = models.EmailField(unique=True)
    #Modelo de tabla de usuarios
    #email, password nombre, ap_pat bio, fecha de nacimiento
    #creación y modificación 
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.TextField(blank = True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

