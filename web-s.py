import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from bs4 import BeautifulSoup
import json

# 1. Pegar conteúdo HTML a partir da URL
url = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path='./chromedriver', options=option)

driver.get(url)
time.sleep(5)

elements = driver.find_elements(by=by.By.XPATH, value="//div[@class='pontocoleta_bloco']")
html_content = [e.get_attribute('outerHTML') for e in elements]
driver.quit()

# 2. Parsear o conteúdo HTML - BeautifulSoup
soup = [BeautifulSoup(div, 'html.parser') for div in html_content]
adresses = []
for s in soup:
    spans = s.find_all('span')
    adresses.append([span.contents for span in spans])

# 3. Transformar dados em um dicionário de dados próprio
address = {}
result = []
for ad in adresses:
    address['ponto'] = str(ad[0][0])
    address['cidade'] = str(ad[1][0])
    address['local'] = str(ad[2][0])
    address['endereco'] = str(ad[3][0])
    address['horario'] = str(ad[4][0])
    address['praca'] = str(ad[6][0])
    result.append(address)

# 4. Converter e salvar em um arquivo JSON
with open('enderecos.json', 'w') as jp:
    js = json.dumps(result, indent=4, ensure_ascii=False)
    jp.write(js)
