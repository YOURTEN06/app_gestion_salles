import customtkinter as ctk
from services.services_salle import ServiceSalle
from tkinter import ttk


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Application de gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()


        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=20, padx=20, fill="x")


        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)


        self.label_description = ctk.CTkLabel(self.cadreInfo, text="Description")
        self.label_description.grid(row=1, column=0, padx=10, pady=10)
        self.entry_description = ctk.CTkEntry(self.cadreInfo)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)


        self.label_categorie = ctk.CTkLabel(self.cadreInfo, text="Catégorie")
        self.label_categorie.grid(row=2, column=0, padx=10, pady=10)
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=10)


        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)


        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=20, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)


        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=20, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )


        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")


        self.treeList.column("code", width=80)
        self.treeList.column("description", width=200)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(fill="both", expand=True)

        self.lister_salles()

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
        self.lister_salles()

    def modifier_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()

        from models.salle import Salle
        from tkinter import messagebox

        salle = Salle(code, description, categorie, capacite)
        succes, message = self.service_salle.modifier_salle(salle)

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

        self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()

        from tkinter import messagebox

        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Succès", "Salle supprimée avec succès")

        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()

        from tkinter import messagebox

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_description.delete(0, "end")
            self.entry_description.insert(0, salle.description)

            self.entry_categorie.delete(0, "end")
            self.entry_categorie.insert(0, salle.categorie)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle non trouvée")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert(
                "",
                "end",
                values=(s.code, s.description, s.categorie, s.capacite)
            )
