from django.db import models

class Inscription(models.Model):
    nom = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200,unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.nom

class Score(models.Model):
    score = models.IntegerField()
    joueur = models.ForeignKey(Inscription,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.score)

