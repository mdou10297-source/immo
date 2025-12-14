import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("data/annonces_clean.csv")

# Convertir les colonnes numériques
df["Surface"] = pd.to_numeric(df["Surface"], errors="coerce")
df["Prix"] = pd.to_numeric(df["Prix"], errors="coerce")
df["Nombre de pièces"] = pd.to_numeric(df["Nombre de pièces"], errors="coerce")

# --- Exemple 1 : Histogramme du nombre de pièces ---
plt.figure(figsize=(8,5))
sns.histplot(df["Nombre de pièces"].dropna(), bins=10, kde=True)
plt.title("Distribution du nombre de pièces")
plt.xlabel("Nombre de pièces")
plt.ylabel("Nombre d'annonces")
plt.show()

# --- Exemple 2 : Scatter plot Surface vs Prix ---
plt.figure(figsize=(8,5))
sns.scatterplot(x="Surface", y="Prix", hue="Type de bien", data=df)
plt.title("Prix vs Surface selon le type de bien")
plt.xlabel("Surface (m²)")
plt.ylabel("Prix (MAD)")
plt.show()

# --- Exemple 3 : Boxplot du prix par type de bien ---
plt.figure(figsize=(8,5))
sns.boxplot(x="Type de bien", y="Prix", data=df)
plt.title("Répartition des prix selon le type de bien")
plt.xlabel("Type de bien")
plt.ylabel("Prix (MAD)")
plt.xticks(rotation=45)
plt.show()
