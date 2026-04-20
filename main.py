from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

salle1 = Salle("A101", "Salle informatique", "Laboratoire", 30)
dao.insert_salle(salle1)

print("Salle ajoutée avec succès")