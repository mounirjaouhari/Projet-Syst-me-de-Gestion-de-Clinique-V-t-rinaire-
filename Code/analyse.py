import pandas as pd
import matplotlib.pyplot as plt

def generer_rapport_activite(clinique):
    consultations = []
    for dossier in clinique.dossiers_medicaux.values():
        for c in dossier.consultations:
            consultations.append({
                "id_consultation": c.id_consultation,
                "id_animal": c.id_animal,
                "date": c.date,
                "motif": c.motif,
                "diagnostic": c.diagnostic,
                "cout": c.cout
            })
    if not consultations:
        print("Aucune consultation à analyser.")
        return

    df = pd.DataFrame(consultations)
    df['date'] = pd.to_datetime(df['date'])

    #Revenu mensuel
    revenu_mensuel = df.groupby(pd.Grouper(key='date', freq='ME'))['cout'].sum()

    print("\n Revenu par mois :")
    for date, total in revenu_mensuel.items():
        print(f"   {date.strftime('%Y-%m')}: {total:.2f} DH")

    #Motifs les plus fréquents
    motifs = df['motif'].value_counts().head(5)
    print("\n Motifs les plus fréquents :")
    for motif, count in motifs.items():
        print(f"   {motif}: {count}")

    # --- Distribution des âges ---
    ages = [a.age for a in clinique.animaux.values()]
    plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
    plt.title("Distribution des âges des animaux")
    plt.xlabel("Âge (ans)")
    plt.ylabel("Nombre d'animaux")
    plt.savefig("rapport_patients.png")
    print("\n📊 Graphique sauvegardé dans 'rapport_patients.png'")
