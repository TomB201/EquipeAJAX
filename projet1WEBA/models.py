from django.db import models

class Equipe(models.Model):
    nom= models.CharField(max_length=64, null=False)
    pays= models.CharField(max_length=64, null=False)

class Maillot(models.Model):
    couleur = models.CharField(max_length=64, null=False)
    marque = models.CharField(max_length=64, null=False)
    type = models.CharField(max_length=32, null=False)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)





