from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# Chemin vers ton chromedriver
service = Service(r"C:/Users/Y_tech/Downloads/139.0.7258.66 chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL de la page des annonces
url = "https://www.vaneau-maroc.com/fr"
driver.get(url)
time.sleep(5)  # laisser le temps à la page de charger

# Récupérer tous les liens des annonces sur la page principale
annonces_links = driver.find_elements(By.CSS_SELECTOR, "a.full-link")
links = [link.get_attribute("href") for link in annonces_links]

# --- Préparation du fichier CSV ---
with open("data/annonces.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # en-têtes
    writer.writerow(["Ville", "Surface", "Nombre de pièces", "Prix", "Type de bien", "Lien"])

    # Parcourir chaque annonce
    for link in links:
        driver.get(link)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Ville
        ville = "Non trouvé"
        if soup.find("h1"):
            ville = soup.find("h1").text.strip()
        
        # Spécifications
        specs = soup.find("div", class_="specifications")
        surface = pièces = prix = "Non trouvé"
        type_bien = "Non trouvé"
        
        if specs:
            # Surface
            surface_span = specs.find(string=lambda t: "surface" in t.lower())
            if surface_span:
                surface = surface_span.find_next("span").text.strip()
            # Nombre de pièces
            pieces_span = specs.find(string=lambda t: "pièces" in t.lower())
            if pieces_span:
                pièces = pieces_span.find_next("span").text.strip()
            # Prix
            prix_span = specs.find(string=lambda t: "prix" in t.lower())
            if prix_span:
                prix = prix_span.find_next("span").text.strip()
                
        # --- Détection du Type de bien depuis le H2 ---
        info_main = soup.find("div", class_="informations__main")
        if info_main:
            h2 = info_main.find("h2")
            if h2:
                h2_text = h2.get_text(separator=" ", strip=True).lower()
                if "villa" in h2_text or "maison" in h2_text:
                    type_bien = "Maison / Villa"
                elif "appartement" in h2_text:
                    type_bien = "Appartement"
                elif "riad" in h2_text:
                    type_bien = "Riad"
                elif "terrain" in h2_text:
                    type_bien = "Terrain"
        
        # Sauvegarde dans le fichier CSV
        writer.writerow([ville, surface, pièces, prix, type_bien, link])
        
        print(f"Enregistré : {ville}, {surface}, {pièces}, {prix}, {type_bien}, {link}")
        print("-" * 40)

driver.quit()
print("✅ Données enregistrées dans annonces.csv")
