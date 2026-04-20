from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

print("=== AJOUT ===")
s1 = Salle("G201", "Salle de conférence", "Bureau", 15)
succes, message = service.ajouter_salle(s1)
print(message)

print("\n=== RECHERCHE ===")
salle = service.rechercher_salle("G201")
if salle:
    print(salle.afficher_infos())

print("\n=== MODIFICATION ===")
s1_modifiee = Salle("G201", "Grande salle de conférence", "Bureau", 22)
succes, message = service.modifier_salle(s1_modifiee)
print(message)

print("\n=== LISTE ===")
for s in service.recuperer_salles():
    print(s.afficher_infos())

print("\n=== SUPPRESSION ===")
service.supprimer_salle("G201")
print("Suppression réussie")