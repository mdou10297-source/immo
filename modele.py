import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Charger les données
df = pd.read_csv("data/annonces_clean.csv")

# Créer une colonne "EstTerrain" : 1 si terrain, 0 sinon
df['EstTerrain'] = df['Type de bien'].apply(lambda x: 1 if x.lower() == 'terrain' else 0)

# Pour les terrains, mettre Nombre de pièces à 0
df.loc[df['EstTerrain'] == 1, 'Nombre de pièces'] = 0

# Définir X et y
X = df[['Surface', 'Nombre de pièces', 'EstTerrain']]
y = df['Prix']

# Diviser en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Sauvegarder le modèle et les colonnes
colonnes_modele = X_train.columns.tolist()
joblib.dump(colonnes_modele, "data/colonnes_modele.pkl")
joblib.dump(model, "data/modele_immobilier.pkl")

print("Modèle sauvegardé sous 'modele_immobilier.pkl'")
