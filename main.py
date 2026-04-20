from Data.dao_salle import DataSalle

dao = DataSalle()
salle = dao.get_salle("A101")

if salle:
    print(salle.afficher_infos())
else:
    print("Salle non trouvée")