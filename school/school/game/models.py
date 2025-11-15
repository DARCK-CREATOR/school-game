from django.db import models

class Inscription(models.Model):
    nom = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to="images",blank=False,null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nom



        
