from datetime import datetime

class Animal:
    _id_counter = 1

    def __init__(self, nom, age, poids):
        self.id_animal = Animal._id_counter
        Animal._id_counter += 1
        self.nom = nom
        self.age = age
        self.poids = poids
        self.espece = "Animal"

    def __str__(self):
        return f"ID: {self.id_animal} {self.nom}, {self.espece}, {self.age} ans, {self.poids} kg"

class Chien(Animal):
    def __init__(self, nom, age, poids, race):
        super().__init__(nom, age, poids)
        self.race = race
        self.espece = "Chien"

    def __str__(self):
        return super().__str__() + f", Race: {self.race}"

class Chat(Animal):
    def __init__(self, nom, age, poids, couleur_pelage):
        super().__init__(nom, age, poids)
        self.couleur_pelage = couleur_pelage
        self.espece = "Chat"

    def __str__(self):
        return super().__str__() + f", Couleur pelage: {self.couleur_pelage}"

class Proprietaire:
    _id_counter = 1

    def __init__(self, nom, adresse):
        self.id_proprietaire = Proprietaire._id_counter
        Proprietaire._id_counter += 1
        self.nom = nom
        self.adresse = adresse
        self.animaux = []

    def __str__(self):
        return f"ID: {self.id_proprietaire} {self.nom}, {self.adresse}, Animaux: {self.animaux}"

class Consultation:
    _id_counter = 1

    def __init__(self, id_animal, motif, diagnostic, cout):
        self.id_consultation = Consultation._id_counter
        Consultation._id_counter += 1
        self.id_animal = id_animal
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.motif = motif
        self.diagnostic = diagnostic
        self.cout = cout

    def __str__(self):
        return f"ID: {self.id_consultation} Animal {self.id_animal}, Date: {self.date}, Motif: {self.motif}, Diagnostic: {self.diagnostic}, Coût: {self.cout} DH"

class DossierMedical:
    def __init__(self, id_animal):
        self.id_animal = id_animal
        self.consultations = []

