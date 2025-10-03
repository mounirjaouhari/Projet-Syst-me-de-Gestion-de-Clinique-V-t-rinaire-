

# 🐾 Système de Gestion pour Clinique Vétérinaire

## **Projet de fin de module Python**
<div align="center">
<img src="https://img.shields.io/badge/Formation-Professionnelle-blue" />
<img src="https://img.shields.io/badge/Jobintech-Ynov_Campus-green" />
<img src="https://img.shields.io/badge/Année-2025--2026-orange" />
<img src="https://img.shields.io/badge/Parcours-Data_Engineer-red" />
</div>
**👥 Équipe de développement :**  
**ADDI Safaa • CHRAA Zakaria • JAOUHARI Mounir • LAMOURI Mohamed Amine**

---



<div align="center">





<div>
  <img src="assets/logo_jobintech.png" alt="Jobintech" width="100" style="margin: 0 20px;">
  <img src="assets/logo_ynov.png" alt="Ynov" width="100" style="margin: 0 20px;">
  
</div>

</div>
---
<div align="center">
<img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Data_Engineering-FF6B35?style=for-the-badge&logo=apachespark&logoColor=white" />
</div>
---


---



Ce projet, réalisé dans le cadre de notre fin de formation, est une application en ligne de commande (CLI) développée en Python pour la gestion complète d'une clinique vétérinaire. Il vise à moderniser le suivi des patients en remplaçant les processus papier par une solution numérique efficace, robuste et facile à utiliser.

## 📁 Structure du Dépôt
```
├── README.md
├── assets/
│   ├── architecture.png
│   ├── class_diagram.png
│   ├── sequence_diagram.png
│   ├── logo_jobintech.png
│   └── logo_ynov.png
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

```
- **📂 `assets/`** : Contient tous les diagrammes UML (Architecture, Classes, Séquence) et logos utilisés pour la conception du projet.
- **🐍 `code/`** : Comprend l'ensemble du code source Python de l'application.
- **📚 `documents/`** : Regroupe les livrables de documentation : le rapport de projet détaillé, la présentation PowerPoint et le Notebook Jupyter explicatif.

## 🏛️ Architecture Logicielle

L'application est bâtie sur une architecture modulaire qui favorise la séparation des responsabilités (Separation of Concerns). Cette approche rend le code plus lisible, maintenable et évolutif.

| Module | Rôle |
|--------|------|
| **`main.py`** (Couche de Présentation) | Point d'entrée qui gère l'interface en ligne de commande (CLI) |
| **`clinique.py`** (Couche Métier / Contrôleur) | Cœur logique de l'application, centralise les opérations métier |
| **`models.py`** (Couche de Données / Modèle) | Définit les classes des entités (Proprietaire, Animal, Consultation) |
| **`persistence.py`** (Couche de Persistance) | Gère la sauvegarde et le chargement des données en JSON |
| **`analyse.py`** (Module d'Analyse) | Génération de rapports avec Pandas et Matplotlib |

## ✨ Fonctionnalités Principales

- ✅ **Gestion des Entités** : CRUD complet pour les propriétaires et les animaux (Chien, Chat)
- ✅ **Dossier Médical** : Enregistrement détaillé des consultations et historique par animal
- ✅ **Persistance Fiable** : Sauvegarde automatique dans un fichier `data.json`
- ✅ **Recherche Avancée** : Recherche par mot-clé dans les diagnostics
- ✅ **Analyse et Rapports** : Génération de statistiques et visualisations
- ✅ **Validation des Saisies** : Contrôles robustes des données utilisateur

## 🚀 Installation et Utilisation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le dépôt :**
```bash
git clone https://github.com/mounirjaouhari/Projet-Syst-me-de-Gestion-de-Clinique-V-t-rinaire-
cd Projet-Syst-me-de-Gestion-de-Clinique-V-t-rinaire-
```

2. **Installer les dépendances :**
```bash
pip install pandas matplotlib
```

3. **Lancer l'application :**
```bash
python code/main.py
```

L'application se lancera dans votre terminal, et un fichier `data.json` sera créé dans le dossier `code/` pour stocker les données.

## 📊 Exemples de Rapports

Le module d'analyse permet de générer :
- 📈 **Revenu mensuel** de la clinique
- 🏥 **Motifs de consultation** les plus fréquents
- 📊 **Histogramme** de la distribution des âges des animaux

## 👨‍💻 Développement

Ce projet a été développé dans le cadre d'un projet de fin de formation, mettant en œuvre les bonnes pratiques de programmation et les principes SOLID.

---
