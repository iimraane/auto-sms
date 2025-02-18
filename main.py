from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Pour envoyer des touches comme "Entrée"
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
user_wants_headless = False

def read_numbers():
    fichier_nom = 'numbers.txt' 
    dossier_recherche = os.getcwd()  

    fichier_trouve = trouver_fichier(fichier_nom, dossier_recherche)

    if fichier_trouve:
        with open(fichier_trouve, 'r') as file:
            numeros = [ligne.strip() for ligne in file.readlines()]
        return numeros
    else:
        print(f"Le fichier {fichier_nom} n'a pas été trouvé dans le répertoire {dossier_recherche}.")
        return [] 

def trouver_fichier(fichier_nom, dossier_recherche):
    for root, dirs, files in os.walk(dossier_recherche):
        if fichier_nom in files:
            return os.path.join(root, fichier_nom) 
    return None  

def first_time_google_messages_connection():


    try:

        driver = webdriver.Chrome()
        driver.get("https://messages.google.com/web") 
        element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/web/authentication') and contains(@class, 'use-without-account-link')]"))
        )
        element.click()
        print("Google Messages Web lancé. Scannez le QR code pour vous connecter.")
        input("Appuyez sur Entrée une fois la connexion terminée...")
        

        numbers_list = read_numbers()
        count = -1
        max_count = len(numbers_list)

        while True:
            element = driver.find_element(By.XPATH, "//mws-icon[contains(@class, 'fab-icon')]")
            element.click()

            time.sleep(0.02)

            input_element = driver.find_element(By.XPATH, "//input[@class='input' and @placeholder='Saisissez un nom, un numéro de téléphone ou une adresse e-mail']")

            count = count+1
            number = numbers_list[count]
            if max_count == count:
                break

            for digit in number:
                input_element.send_keys(digit)
                time.sleep(0.001)  

            time.sleep(0.1)

            input_element.send_keys(Keys.RETURN)
            

            message_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Message']"))
            )        
            message = "Hello, c'est un message envoyé via Selenium!"

            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)


            time.sleep(0.2)

    except Exception as e:
        print(f"Erreur lors de la connexion à Google Messages Web : {e}")

if __name__ == "__main__":
    print("Démarrage pour la première connexion à Google Messages Web...")
    first_time_google_messages_connection()
