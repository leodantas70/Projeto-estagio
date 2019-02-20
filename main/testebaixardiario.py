import hashlib
import re
import requests
import time

from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.

browser = webdriver.Chrome('/home/leodantas/pythom/chromedriver', chrome_options=chrome_options)
browser.get("http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/")
nav = browser.find_element_by_id("divDiarioLast")
time.sleep (2)

text2 = nav.text
arq2 = open("texto2.csv","w")
arq2.write(text2)
arq2.close()

browser.get("http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diarioInSession.do?action=buscarDiarios&voDiarioSearch.listState.index=6")
nav = browser.find_element_by_tag_name('body')
time.sleep(2)

nav1 = nav.text
arq2 = open("texto3.csv","w")
arq2.write(nav1)
arq2.close()



input_data_inicial = input('Digite a data dia/mes/ano: ')


resultado = re.search(input_data_inicial,text2)

print ("")
textUtf8 = input_data_inicial.encode("utf-8")
hash = hashlib.md5(textUtf8)
hexa = hash.hexdigest()
if resultado == None:
    print ("Nao exite essa data")
else:

    print ("Seu hash é: ", hexa)
