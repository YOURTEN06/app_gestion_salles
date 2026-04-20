from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

s1 = Salle("B201", "Salle de cours", "Classe", 25)
dao.insert_salle(s1)
print("Ajout réussi")

salle = dao.get_salle("B201")
if salle:
    print("Recherche :", salle.afficher_infos())

s1_modifiee = Salle("B201", "Grande salle de cours", "Classe", 40)
dao.update_salle(s1_modifiee)
print("Modification réussie")

print("Liste des salles :")
for s in dao.get_salles():
    print(s.afficher_infos())

dao.delete_salle("B201")
print("Suppression réussie")