import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Charger le CSV nettoyé
df = pd.read_csv("data/annonces_clean.csv")

# Encoder les colonnes catégorielles
le_ville = LabelEncoder()
le_type = LabelEncoder()

df["Ville_enc"] = le_ville.fit_transform(df["Ville"])
df["Type_bien_enc"] = le_type.fit_transform(df["Type de bien"])

# Sélection des features et de la cible
X = df[["Surface", "Nombre de pièces", "Ville_enc", "Type_bien_enc"]]
y = df["Prix"]

# Normalisation des features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
