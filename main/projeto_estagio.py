import hashlib
import re
import requests
import time

import selenium.webdriver.common.keys

from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome('/home/leodantas/pythom/chromedriver', chrome_options=chrome_options)
browser.get("http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/")
select = browser.find_element_by_name("voDiarioSearch.dataPubFim")
input_data_inicial = input('Digite a data dia/mês/ano: ')
select.send_keys(input_data_inicial)
select.send_keys(Keys.ENTER)
time.sleep(1)
buscardata = browser.find_element_by_id('divDiarioTextual')
datatxt = buscardata.text
resultado = re.search(input_data_inicial,datatxt)
print ("")
textUtf8 = input_data_inicial.encode("utf-8")
hash = hashlib.md5(textUtf8)
hexa = hash.hexdigest()
if resultado == None:
    print ("Nao exite essa data")
else:
    print ("Seu hash é: ", hexa)
