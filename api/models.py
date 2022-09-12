from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
	matricule = models.PositiveIntegerField()
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user.nom} {self.user.prenom} avec comme matricule Num. {self.matricule}" 

class Client(models.Model):
	nom = models.CharField(max_length=30,blank=False,null=False)
	prenom = models.CharField(max_length=30,blank=False,null=False)
	telephone = models.PositiveIntegerField()
	details =  models.TextField()

	def __str__(self):
		return f"{self.nom} {self.prenom} : {self.telephone}" 

class Chambre(models.Model):
	numero = models.PositiveIntegerField(default=0)
	typeChambre = models.CharField(max_length=30)
	prix_chambre = models.PositiveIntegerField(default=0)
	is_disponible = models.BooleanField()

	def __str__(self):
		return f" chambre numero: {self.numero} de type {self.typeChambre} est {self.is_disponible}" 


class Reservation(models.Model):
	id =  models.SmallIntegerField(primary_key=True)
	date_debut = models.DateTimeField(auto_now_add=True)
	date_fin = models.DateTimeField()
	chambre = models.ForeignKey("Chambre",on_delete=models.PROTECT)
	client = models.ForeignKey("Client",on_delete=models.PROTECT)

	def __str__(self):
		return f"chambre {self.chambre.numero} est réservée du {self.date_debut} au {self.date_fin} " 

class Paiement(models.Model):
	montant = models.PositiveIntegerField(default=0)
	motif = models.CharField(max_length=30)
	client = models.ForeignKey("Client",on_delete=models.PROTECT)

	def __str__(self):
		return f"montant payé: {self.montant} par {self.client.nom} {self.client.prenom}" 


class Commande(models.Model):
	nom_produit = models.CharField(max_length=30)
	quantite = models.PositiveIntegerField(default=0)
	prix = models.FloatField(default=0.0)
	client = models.ForeignKey("Client",on_delete=models.PROTECT)

	def __str__(self):
		return f"commande de {self.nom_produit} par {self.client.nom} {self.client.prenom}" 
