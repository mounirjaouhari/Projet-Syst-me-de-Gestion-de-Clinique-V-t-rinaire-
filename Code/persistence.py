import json, os
from models import Proprietaire, Chien, Chat, Consultation, DossierMedical, Animal

def sauvegarder(clinique, fichier="data.json"):
    data = {
        "proprietaires": {pid: vars(p) for pid, p in clinique.proprietaires.items()},
        "animaux": {aid: vars(a) for aid, a in clinique.animaux.items()},
        "dossiers_medicaux": {
            str(aid): [vars(c) for c in d.consultations]
            for aid, d in clinique.dossiers_medicaux.items()
        }
    }
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)

def charger(clinique, fichier="data.json"):
    if not os.path.exists(fichier) or os.path.getsize(fichier) == 0:
        print("-> Première utilisation.")
        return

    with open(fichier, "r") as f:
        data = json.load(f)

    clinique.proprietaires = {}
    for pid, p_data in data.get("proprietaires", {}).items():
        p = Proprietaire(p_data['nom'], p_data['adresse'])
        p.id_proprietaire = p_data['id_proprietaire']
        p.animaux = p_data['animaux']
        clinique.proprietaires[p.id_proprietaire] = p

    clinique.animaux = {}
    for aid, a_data in data.get("animaux", {}).items():
        if a_data['espece'] == "Chien":
            a = Chien(a_data['nom'], a_data['age'], a_data['poids'], a_data.get('race',''))
        elif a_data['espece'] == "Chat":
            a = Chat(a_data['nom'], a_data['age'], a_data['poids'], a_data.get('couleur_pelage',''))
        else:
            continue
        a.id_animal = a_data['id_animal']
        clinique.animaux[a.id_animal] = a

    clinique.dossiers_medicaux = {}
    for aid, c_list in data.get("dossiers_medicaux", {}).items():
        dossier = DossierMedical(int(aid))
        for c_data in c_list:
            c = Consultation(c_data['id_animal'], c_data['motif'], c_data['diagnostic'], c_data['cout'])
            c.id_consultation = c_data['id_consultation']
            c.date = c_data['date']
            dossier.consultations.append(c)
        clinique.dossiers_medicaux[int(aid)] = dossier


def remettre_a_jour_compteurs(clinique):
    """ Ajuste les compteurs d'ID après le chargement des données """
    if clinique.animaux:
        Animal._id_counter = max(a.id_animal for a in clinique.animaux.values()) + 1
    else:
        Animal._id_counter = 1

    if clinique.proprietaires:
        Proprietaire._id_counter = max(p.id_proprietaire for p in clinique.proprietaires.values()) + 1
    else:
        Proprietaire._id_counter = 1

    toutes_consultations = [c for d in clinique.dossiers_medicaux.values() for c in d.consultations]
    if toutes_consultations:
        Consultation._id_counter = max(c.id_consultation for c in toutes_consultations) + 1
    else:
        Consultation._id_counter = 1
