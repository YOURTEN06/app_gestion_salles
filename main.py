from Data.dao_salle import DataSalle

dao = DataSalle()
liste = dao.get_salles()

for salle in liste:
    print(salle.afficher_infos())