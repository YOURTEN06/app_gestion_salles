import customtkinter as ctk
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Application de gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=20, padx=20, fill="x")

        # Code
        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        # Description
        self.label_description = ctk.CTkLabel(self.cadreInfo, text="Description")
        self.label_description.grid(row=1, column=0, padx=10, pady=10)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)

        # Catégorie
        self.label_categorie = ctk.CTkLabel(self.cadreInfo, text="Catégorie")
        self.label_categorie.grid(row=2, column=0, padx=10, pady=10)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=10)

        # Capacité
        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)

        # Cadre Actions
        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=20, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        from models.salle import Salle

        salle = Salle(code, description, categorie, capacite)
        succes, message = self.service_salle.ajouter_salle(salle)

        from tkinter import messagebox

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)