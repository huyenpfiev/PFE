
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#client = MongoClient('mongodb+srv://DinhHuyen:Huyendien13-08@cluster0-mlysy.mongodb.net/')
client=MongoClient("mongodb://localhost:27017/")

# Options headless driver
options = Options()
options.headless = True

# Initialisation driver
driver = webdriver.Firefox(options=options,executable_path = '/usr/local/bin/geckodriver')

class MongoRepository(object):
  def __init__(self):
    self.db = client.PFE

  def login(self, user):
    return self.db.users.find(user[0])
  

  def register(self,user):
    prenom=user[0]['FirstName']
    nom=user[0]['LastName']
    # Acceder au site de dblp
    driver.get("https://dblp.uni-trier.de")
    # Saisie du nom d'un auteur dans la barre de recherche
    element = driver.find_element_by_name("q")
    element.send_keys(prenom + " " + nom)
    # Attente de l'affichage de la liste des publications
    wait = WebDriverWait(driver, 1)
    publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'completesearch-publs')))
    # Recuperation de la liste des resultats
    html_list = driver.find_elements_by_class_name("result-list")
  
    if len(html_list)==0:
      return 0
    else :
      items = html_list[0].find_elements_by_tag_name("li")
      return items  

  def saveAcc(self,user):
    us= self.db.users.find({'Username':user[0]['Username']})
    i=0
    for u in us:
      i=i+1
    
    if i>0:
      return 0
    else:
      self.db.users.insert_one(user[0])    
      return 1

  def getPubs(self,user):
    choix =user[0]['source']
    prenom=user[0]['FirstName']
    nom=user[0]['LastName']
    array=[]
    # Acceder au site de dblp
    driver.get("https://dblp.uni-trier.de")
    # Saisie du nom d'un auteur dans la barre de recherche
    element = driver.find_element_by_name("q")
    element.send_keys(prenom + " " + nom)
    # Attente de l'affichage de la liste des publications
    wait = WebDriverWait(driver, 1)
    publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'completesearch-publs')))
    # Recuperation de la liste des resultats
    html_list = driver.find_elements_by_class_name("result-list")
    # Nom de l'auteur
    name=html_list[0].find_elements_by_tag_name("li")
    array.append(name[choix].text)
    #Liste des URL
    homonym = driver.find_elements_by_xpath("//ul[@class='result-list']/li/a")
     
    page = homonym[int(choix)]
    driver.get(page.get_attribute("href"))
    # Attente de l'affichage de la liste des publications
    wait = WebDriverWait(driver, 1)
    publication_results = wait.until(EC.visibility_of_element_located((By.ID, 'publ-section')))
    # Index des articles
    pubs = driver.find_elements_by_class_name("title")
    articles=[]
    for i in pubs:
      articles.append(i.text)
    array.append(articles)
    
    # Index des coauteurs
    coauthors = driver.find_elements_by_xpath("//div[@class='person']/a")
    coauteurs=[]
    for i in coauthors:
      coauteurs.append(i.get_attribute('innerHTML')) 
    array.append(coauteurs)
    
    return array


