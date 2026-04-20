from Data.dao_salle import DataSalle

dao = DataSalle()
dao.delete_salle("A101")

print("Salle supprimée avec succès")