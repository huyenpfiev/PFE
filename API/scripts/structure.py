from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Options headless driver
options = Options()
options.headless = True

# Initialisation driver
driver = webdriver.Firefox(options=options,executable_path = '/usr/local/bin/geckodriver')

# Acceder au site de dblp
driver.get("https://dblp.uni-trier.de")

# Saisie du nom d'un auteur dans la barre de recherche
element = driver.find_element_by_name("q")
element.send_keys("durand nicolas")

# Attente de l'affichage de la liste des publications
wait = WebDriverWait(driver, 10)
publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'completesearch-publs')))

# Recuperation de la liste des resultats
html_list = driver.find_elements_by_class_name("result-list")

# Exact matches
items = html_list[0].find_elements_by_tag_name("li")
print("Exact matches : ", len(items))
for item in items:
    text = item.text
    print(text)
# Likely matches
if len(html_list)>1:
    items = html_list[1].find_elements_by_tag_name("li")
    print("Likely matches : ", len(items))
    for item in items:
        text = item.text
        print(text)

driver.quit()