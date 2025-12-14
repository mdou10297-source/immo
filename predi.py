import pandas as pd
import joblib

# --- Charger le modèle et les colonnes ---
model = joblib.load("modele_immobilier.pkl")

colonnes_modele = joblib.load("colonnes_modele.pkl")


# --- Entrée utilisateur ---
surface = float(input("Entrez la surface en m² : "))
pieces = int(input("Entrez le nombre de pièces (mettre 0 si terrain) : "))
type_bien = input("Entrez le type de bien (Appartement, Maison / Villa, Terrain) : ")

# --- Créer un DataFrame vide ---
df_input = pd.DataFrame(columns=colonnes_modele)
df_input.loc[0] = 0  # remplir toutes les colonnes avec des zéros

# --- Remplir les colonnes numériques ---
if 'Surface' in df_input.columns:
    df_input.at[0, 'Surface'] = surface

# Remplir le nombre de pièces seulement si ce n'est pas un terrain
if type_bien.lower() != 'terrain' and 'Nombre de pièces' in df_input.columns:
    df_input.at[0, 'Nombre de pièces'] = pieces

# --- Encoder le type de bien ---
col_type = f"Type de bien_{type_bien}"
if col_type in df_input.columns:
    df_input.at[0, col_type] = 1
else:
    print(f"⚠ Attention : type de bien '{type_bien}' non reconnu. Valeur par défaut utilisée.")

# --- Prédiction ---
prix_pred = model.predict(df_input)
print(f"Prix prédit : {prix_pred[0]:,.2f} €")
