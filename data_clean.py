import pandas as pd
import numpy as np

# Charger le fichier CSV
df = pd.read_csv("data/annonces_clean.csv")


# Supprimer la colonne Lien si elle existe
if "Lien" in df.columns:
    df = df.drop(columns=["Lien"])

# Nettoyage de la colonne Surface
df["Surface"] = df["Surface"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Surface"] = df["Surface"].replace("", np.nan).astype(float)

# Nettoyage de la colonne Nombre de pièces
df["Nombre de pièces"] = df["Nombre de pièces"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Nombre de pièces"] = df["Nombre de pièces"].replace("", np.nan).astype(float)

# Nettoyage de la colonne Prix
df["Prix"] = df["Prix"].astype(str).str.replace(r"[^\d]", "", regex=True)
df["Prix"] = df["Prix"].replace("", np.nan).astype(float)

# Afficher les 5 premières lignes pour vérifier
print(df.head())

# Sauvegarder le fichier nettoyé
df.to_csv("data/annonces_clean.csv", index=False)
