from clinique import Clinique
from persistence import sauvegarder, charger, remettre_a_jour_compteurs
from analyse import generer_rapport_activite

clinique = Clinique()

try:
    charger(clinique)
    print("Données chargées avec succès.")
except FileNotFoundError:
    print("Première utilisation : aucune donnée trouvée, base initialisée vide.")
except Exception as e:
    print("Erreur au chargement :", e)

remettre_a_jour_compteurs(clinique)

def input_nonvide(prompt):
    while True:
        val = input(prompt).strip()
        if val == "0":
            return None
        if val:
            return val
        print("Champ obligatoire, veuillez réessayer.")

def input_int(prompt):
    while True:
        val = input_nonvide(prompt)
        if val is None:
            return None
        if val.isdigit():
            return int(val)
        print("Veuillez entrer un entier valide.")

def input_float(prompt):
    while True:
        val = input_nonvide(prompt)
        if val is None:
            return None
        try:
            return float(val)
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def input_email(prompt):
    while True:
        val = input_nonvide(prompt)
        if val is None:
            return None
        if "@" in val:
            return val.lower()
        print("Email invalide, doit contenir '@'.")

def menu():
    print("\n===== CLINIQUE VÉTÉRINAIRE =====")
    print("1. Ajouter un propriétaire")
    print("2. Ajouter un animal")
    print("3. Lister tous les animaux")
    print("4. Lister animaux d'un propriétaire")
    print("5. Enregistrer une consultation")
    print("6. Historique d'un animal")
    print("7. Rechercher diagnostic")
    print("8. Générer rapport activité")
    print("0. Quitter")

while True:
    menu()
    choix = input_nonvide("Choisir une option: ")
    if choix is None or choix == "0":
        print("Au revoir !")
        break

    elif choix == "1":
        nom = input_nonvide("Nom du propriétaire (0 pour annuler): ")
        if nom is None:
            continue
        email = input_email("Adresse email (0 pour annuler): ")
        if email is None:
            continue
        p = clinique.ajouter_proprietaire(nom, email)
        sauvegarder(clinique)
        print(f"Propriétaire ajouté: ID {p.id_proprietaire} - {p.nom}")

    elif choix == "2":
        if not clinique.proprietaires:
            print("Aucun propriétaire disponible.")
            continue
        valid_types = ["chien", "chat"]
        while True:
            type_a = input_nonvide("Type animal (Chien/Chat) (0 pour annuler): ")
            if type_a is None:
                break
            if type_a.lower() not in valid_types:
                print("Type inconnu. Veuillez entrer 'Chien' ou 'Chat'.")
                continue
            type_a = type_a.capitalize()
            break
        if type_a is None:
            continue

        while True:
            nom = input_nonvide("Nom (0 pour annuler): ")
            if nom is None:
                break
            if not nom.isalpha():
                print("Nom invalide. Utilisez uniquement des lettres.")
                continue
            break
        if nom is None:
            continue

        while True:
            age = input_int("Âge (ans) (0 pour annuler): ")
            if age is None:
                break
            if age <= 0:
                print("L'âge doit être supérieur à 0.")
                continue
            break
        if age is None:
            continue

        while True:
            poids = input_float("Poids (kg) (0 pour annuler): ")
            if poids is None:
                break
            if poids <= 0:
                print("Le poids doit être supérieur à 0.")
                continue
            break
        if poids is None:
            continue

        if type_a.lower() == "chien":
            while True:
                info_sup = input_nonvide("Race (0 pour annuler): ")
                if info_sup is None:
                    break
                if not info_sup.isalpha():
                    print("Race invalide. Utilisez uniquement des lettres.")
                    continue
                break
        elif type_a.lower() == "chat":
            while True:
                info_sup = input_nonvide("Couleur pelage (0 pour annuler): ")
                if info_sup is None:
                    break
                if not info_sup.isalpha():
                    print("Couleur invalide. Utilisez uniquement des lettres.")
                    continue
                break
        if info_sup is None:
            continue

        print("Propriétaires disponibles :")
        for p in clinique.proprietaires.values():
            print(f" - ID {p.id_proprietaire} : {p.nom}")

        while True:
            id_proprio = input_int("ID du propriétaire (0 pour annuler): ")
            if id_proprio is None:
                break
            if id_proprio not in clinique.proprietaires:
                print("Propriétaire non trouvé.")
                continue
            break
        if id_proprio is None:
            continue

        a = clinique.ajouter_animal(type_a, nom, age, poids, info_sup, id_proprio)
        sauvegarder(clinique)
        print(f"Animal ajouté: ID {a.id_animal} - {a.nom}")

    elif choix == "3":
        clinique.lister_animaux()

    elif choix == "4":
        id_p = input_int("ID du propriétaire (0 pour annuler): ")
        if id_p is None:
            continue
        clinique.animaux_proprietaire(id_p)

    elif choix == "5":
        id_a = input_int("ID de l'animal (0 pour annuler): ")
        if id_a is None:
            continue
        motif = input_nonvide("Motif (0 pour annuler): ")
        if motif is None:
            continue
        diagnostic = input_nonvide("Diagnostic (0 pour annuler): ")
        if diagnostic is None:
            continue
        while True:
            cout = input_float("Coût (MAD) (0 pour annuler): ")
            if cout is None:
                break
            if cout < 0:
                print("Le coût doit être positif.")
                continue
            break
        if cout is None:
            continue
        c = clinique.enregistrer_consultation(id_a, motif, diagnostic, cout)
        if c:
            sauvegarder(clinique)
            print(f"Consultation enregistrée: ID {c.id_consultation} - {c.motif}")

    elif choix == "6":
        id_a = input_int("ID de l'animal (0 pour annuler): ")
        if id_a is None:
            continue
        clinique.afficher_historique(id_a)

    elif choix == "7":
        mot = input_nonvide("Mot-clé diagnostic (0 pour annuler): ")
        if mot is None:
            continue
        res = clinique.recherche_diagnostic(mot)
        if res:
            print("Résultats :")
            for c in res:
                print(f" - ID {c.id_consultation} : {c.motif} / {c.diagnostic}")
        else:
            print("Aucun résultat trouvé.")

    elif choix == "8":
        generer_rapport_activite(clinique)

    else:
        print("Option invalide.")
