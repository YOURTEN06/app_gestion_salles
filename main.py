from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Ajout
s1 = Salle("E404", "Salle multimédia", "Classe", 28)
dao.insert_salle(s1)
print("Ajout réussi")

# Recherche
salle = dao.get_salle("E404")
if salle:
    print("Recherche :", salle.afficher_infos())

# Modification
s1_modifiee = Salle("E404", "Grande salle multimédia", "Classe", 35)
dao.update_salle(s1_modifiee)
print("Modification réussie")

# Affichage de toutes les salles
print("Liste des salles :")
for s in dao.get_salles():
    print(s.afficher_infos())

# Suppression
dao.delete_salle("E404")
print("Suppression réussie")