from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

salle = Salle("F101", "Salle test modifiée", "Classe", 35)
succes, message = service.modifier_salle(salle)

print(message)