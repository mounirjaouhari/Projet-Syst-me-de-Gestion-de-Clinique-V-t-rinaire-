📂 Système de Gestion pour Clinique Vétérinaire
Ce projet, réalisé dans le cadre de notre fin de formation, est une application en ligne de commande (CLI) développée en Python pour la gestion complète d'une clinique vétérinaire. Il vise à moderniser le suivi des patients en remplaçant les processus papier par une solution numérique efficace, robuste et facile à utiliser.

🌳 Structure du Dépôt
Voici l'arborescence des fichiers de ce projet :

.
├── README.md
├── assets/
│   ├── architecture.png
│   ├── class_diagram.png
│   └── sequence_diagram.png
├── code/
│   ├── __main__.py
│   ├── clinique.py
│   ├── models.py
│   ├── persistence.py
│   ├── analyse.py
│   └── data.json
└── documents/
    ├── rapport_projet.docx
    ├── presentation_projet.pptx
    └── notebook_documentation.ipynb
assets/ : Contient tous les diagrammes UML (Architecture, Classes, Séquence) utilisés pour la conception du projet.

code/ : Comprend l'ensemble du code source Python de l'application.

documents/ : Regroupe les livrables de documentation : le rapport de projet détaillé, la présentation PowerPoint et le Notebook Jupyter explicatif.

🏛️ Architecture Logicielle
L'application est bâtie sur une architecture modulaire qui favorise la séparation des responsabilités (Separation of Concerns). Cette approche rend le code plus lisible, maintenable et évolutif.

Shutterstock

main.py (Couche de Présentation) : C'est le point d'entrée qui gère l'interface en ligne de commande (CLI). Il est responsable de l'affichage des menus, de la capture des saisies utilisateur et de l'orchestration des appels à la couche métier.

clinique.py (Couche Métier / Contrôleur) : Le cœur logique de l'application. La classe Clinique centralise toutes les opérations métier (ajouter un propriétaire, enregistrer une consultation, etc.) et manipule les objets du modèle.

models.py (Couche de Données / Modèle) : Définit les "plans" de nos données à travers des classes Python (Proprietaire, Animal, Consultation). Il encapsule les attributs et les comportements de base des entités du domaine.

persistence.py (Couche de Persistance) : Gère la sauvegarde et le chargement de l'état de l'application. Il convertit les objets Python en format JSON pour les stocker sur le disque et effectue l'opération inverse au démarrage.

analyse.py (Module d'Analyse) : Module spécialisé dans le traitement des données pour la génération de rapports. Il utilise les bibliothèques Pandas et Matplotlib pour créer des statistiques et des visualisations.

✨ Fonctionnalités Principales
Gestion des Entités : CRUD (Créer, Lire, Mettre à jour, Supprimer) complet pour les propriétaires et les animaux (Chien, Chat).

Dossier Médical : Enregistrement détaillé de chaque consultation (motif, diagnostic, coût) et consultation de l'historique complet par animal.

Persistance Fiable : Sauvegarde automatique de toutes les données dans un fichier data.json après chaque modification.

Recherche Avancée : Fonction de recherche par mot-clé dans les diagnostics des consultations.

Analyse et Rapports : Génération de rapports d'activité incluant le revenu mensuel, les motifs de consultation les plus fréquents et un histogramme de la distribution des âges des animaux.

Validation des Saisies : Des contrôles robustes sont en place pour garantir que les données saisies par l'utilisateur (nombres, textes non vides) sont valides.

🚀 Installation et Utilisation
Pour lancer le projet sur votre machine locale, suivez ces étapes :

Cloner le dépôt :

Bash

git clone https://github.com/votre-nom-utilisateur/votre-repo.git
cd votre-repo
Installer les dépendances :
Le projet nécessite pandas et matplotlib pour la génération des rapports.

Bash

pip install pandas matplotlib
Lancer l'application :
Exécutez le module main.py depuis le dossier code/.

Bash

python code/main.py
L'application se lancera dans votre terminal, et un fichier data.json sera créé dans le dossier code/ pour stocker les données.