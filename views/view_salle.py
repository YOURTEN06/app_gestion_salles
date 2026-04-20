import customtkinter as ctk
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Application de gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()