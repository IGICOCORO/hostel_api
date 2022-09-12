from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = "id","matricule","user"
	search_fields = "id","matricule","user"

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = "id","nom","prenom","telephone","details"
	search_fields = "id","nom","prenom","telephone","details"
    

@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
	list_display = "id", "numero","typeChambre","prix_chambre","is_disponible"
	search_fields = "id", "numero","prix_chambre","is_disponible" 
    

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = "id","date_debut","date_fin","chambre","client"
	search_fields = "id","date_debut","date_fin","chambre","client"

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
	list_display = "id","montant","motif","client"
	search_fields = "id","montant","client"

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
	list_display = "id","nom_produit","quantite","prix","client"
	search_fields = "id","nom_produit","quantite","prix"