from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Options headless driver
options = Options()
options.headless = True

# Initialisation driver
driver = webdriver.Firefox(options=options,executable_path = '/usr/local/bin/geckodriver')

prenom = "nicolas"
nom = "durand"

# Acceder a la page de l'auteur
driver.get("https://dblp.uni-trier.de/search?q=" + prenom + " " + nom)
'''
try :
    # Attente de l'affichage de la liste des publications
    wait = WebDriverWait(driver, 3)
    publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'publ-section')))
    # Index des articles
    liste = driver.find_elements_by_class_name("title")
    print("Auteur : " + p.replace('_',' ') + " " + nom.capitalize())
    print("Nombre d'articles : " + str(len(liste)))
    # Index des coauteurs
    liste = driver.find_elements_by_xpath("//div[@class='person']/a")
    print("Nombre de coauteurs : " + str(len(liste)))

# Element 'publ-section' n'a pas ete trouve --> Auteur n'existe pas ou Plusieurs resultats possibles
except TimeoutException :
'''
    # Acceder au site de dblp
driver.get("https://dblp.uni-trier.de")
    # Saisie du nom d'un auteur dans la barre de recherche
element = driver.find_element_by_name("q")
element.send_keys(prenom + " " + nom)
    # Attente de l'affichage de la liste des publications
wait = WebDriverWait(driver, 3)
publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'completesearch-publs')))
    # Recuperation de la liste des resultats
html_list = driver.find_elements_by_class_name("result-list")
    # Liste des URL
homonym = driver.find_elements_by_xpath("//ul[@class='result-list']/li/a")
    
if len(html_list)==0:
    print("Pas de resultats pour : " + prenom.capitalize() + " " + nom.capitalize())
else :
    print("Plusieurs resultats pour : " + prenom.capitalize() + " " + nom.capitalize())
        # Exact matches
    print("========== EXACT MATCHES ==========")
    items = html_list[0].find_elements_by_tag_name("li")
    print("Nombre de resultats : ", len(items))
    print("========================================")
    i = 1
    for item in items:
        print("Choix " + str(i))
        text = item.text
        print(text)
        print("========================================")
        i = i+1
    if len(html_list)>1:
            # Likely matches
        print("========== LIKELY MATCHES ==========")
        items = html_list[1].find_elements_by_tag_name("li")
        print("Nombre de resultats : ", len(items))
        print("========================================")
        for item in items:
            print("Choix " + str(i))
            text = item.text
            print(text)
            print("========================================")
            i = i+1
        
    res = input("Saisir votre choix : ")
    page = homonym[int(res)-1]
        #print(page.get_attribute("href"))
    driver.get(page.get_attribute("href"))
        # Attente de l'affichage de la liste des publications
    wait = WebDriverWait(driver, 3)
    publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'publ-section')))
        # Index des articles
    liste = driver.find_elements_by_class_name("title")
        # Nom de l'auteur
    name = driver.find_element_by_xpath("//span[@class='name primary']")
    print("Auteur : " + name.text)
    print("Nombre d'articles : " + str(len(liste)))
        # Index des coauteurs
    coauteurs = driver.find_elements_by_xpath("//div[@class='person']/a")
    print("Nombre de coauteurs : " + str(len(coauteurs)))   
    
#finally :
driver.quit()