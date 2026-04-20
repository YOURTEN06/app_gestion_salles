from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

salle1 = Salle("A101", "Salle réseau", "Laboratoire", 35)
dao.update_salle(salle1)

print("Salle modifiée avec succès")