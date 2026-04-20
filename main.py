from services.services_salle import ServiceSalle

service = ServiceSalle()

print("Recherche d'une salle :")
salle = service.rechercher_salle("F101")
if salle:
    print(salle.afficher_infos())
else:
    print("Salle non trouvée")

print("\nListe des salles :")
for s in service.recuperer_salles():
    print(s.afficher_infos())

print("\nSuppression de la salle F101")
service.supprimer_salle("F101")
print("Suppression réussie")