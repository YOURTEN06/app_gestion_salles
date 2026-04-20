from Data.dao_salle import DataSalle

dao = DataSalle()
connexion = dao.get_connection()

if connexion.is_connected():
    print("Connexion à MySQL réussie")

connexion.close()