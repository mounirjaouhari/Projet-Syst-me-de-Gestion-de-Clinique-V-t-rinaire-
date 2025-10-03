from models import Proprietaire, Chien, Chat, Consultation, DossierMedical

class Clinique:
    def __init__(self):
        self.proprietaires = {}
        self.animaux = {}
        self.dossiers_medicaux = {}

    def ajouter_proprietaire(self, nom, adresse):
        p = Proprietaire(nom, adresse)
        self.proprietaires[p.id_proprietaire] = p
        return p

    def rechercher_proprietaire(self, nom):
        return [p for p in self.proprietaires.values() if nom.lower() in p.nom.lower()]

    def ajouter_animal(self, type_animal, nom, age, poids, info_sup, id_proprio):
        if type_animal.lower() == "chien":
            a = Chien(nom, age, poids, info_sup)
        elif type_animal.lower() == "chat":
            a = Chat(nom, age, poids, info_sup)
        else:
            return None
        self.animaux[a.id_animal] = a
        self.proprietaires[id_proprio].animaux.append(a.id_animal)
        return a

    def lister_animaux(self):
        if not self.animaux:
            print("⚠️ Aucun animal enregistré.")
            return
        print("🐾 Liste des animaux :")
        for a in self.animaux.values():
            print(" ", a)

    def animaux_proprietaire(self, id_proprio):
        p = self.proprietaires.get(id_proprio)
        if not p:
            print("❌ Propriétaire non trouvé")
            return
        print(f"🐾 Animaux du propriétaire {p.nom} :")
        for aid in p.animaux:
            print(" ", self.animaux.get(aid))

    def enregistrer_consultation(self, id_animal, motif, diagnostic, cout):
        if id_animal not in self.animaux:
            print("❌ Animal non trouvé")
            return None
        c = Consultation(id_animal, motif, diagnostic, cout)
        if id_animal not in self.dossiers_medicaux:
            self.dossiers_medicaux[id_animal] = DossierMedical(id_animal)
        self.dossiers_medicaux[id_animal].consultations.append(c)
        return c

    def afficher_historique(self, id_animal):
        dossier = self.dossiers_medicaux.get(id_animal)
        if not dossier:
            print("⚠️ Aucun dossier médical pour cet animal")
            return
        print(f"📄 Historique médical de l'animal {self.animaux[id_animal].nom} :")
        for c in sorted(dossier.consultations, key=lambda x: x.date):
            print(" ", c)

    def recherche_diagnostic(self, mot_cle):
        resultats = []
        for dossier in self.dossiers_medicaux.values():
            for c in dossier.consultations:
                if mot_cle.lower() in c.diagnostic.lower():
                    resultats.append(c)
        return resultats
