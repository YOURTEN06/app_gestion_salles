from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

salle = Salle("F101", "Salle de test", "Classe", 20)
succes, message = service.ajouter_salle(salle)

print(message)