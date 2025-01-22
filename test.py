from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# Configuration des options Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')  # Mode headless
chrome_options.add_argument('--disable-gpu')  # Désactiver l'accélération GPU (utile sur certains systèmes)
chrome_options.add_argument('--no-sandbox')  # Nécessaire sur certains environnements Linux
chrome_options.add_argument('--disable-dev-shm-usage')  # Évite les problèmes de mémoire partagée
chrome_options.add_argument('--window-size=1920,1080')  # Taille de fenêtre pour les captures d'écran ou le rendu


service = Service('/usr/bin/chromedriver')  # Chemin par défaut pour le gestionnaire de paquets

# Lancement du navigateur avec les options
#options=chrome_options
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://127.0.0.1:8000/")

select_element = driver.find_element(By.NAME, 'action')
select = Select(select_element)
select.select_by_index(0)

driver.find_element(By.NAME, "research").click()

time.sleep(1)

try:
    flag = driver.find_element(By.ID, 'flag')
    print("Test 1 OK")
except:
    exit(1)

driver.get("http://127.0.0.1:8000/")

select_element = driver.find_element(By.NAME, 'action')
select = Select(select_element)
select.select_by_index(1)
driver.find_element(By.NAME, "research").click()

try:
    flag = driver.find_element(By.ID, 'flag')
    print("Test 2 OK")
except:
    exit(1)

driver.quit()