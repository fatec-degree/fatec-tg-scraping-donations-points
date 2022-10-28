from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from bs4 import BeautifulSoup
import json
import time


def create_driver():
    option = Options()
    option.headless = True
    return webdriver.Chrome(executable_path='resources/chromedriver', options=option)


def get_html_content(url, driver):
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements(by=by.By.XPATH, value="//div[@class='pontocoleta_bloco']")
    html = [e.get_attribute('outerHTML') for e in elements]
    driver.quit()
    return html


def get_donation_points(html):
    soup = [BeautifulSoup(div, 'html.parser') for div in html]
    adresses = []
    for s in soup:
        spans = s.find_all('span')
        adresses.append([span.contents for span in spans])
    return adresses


def transform_data(data):
    address = {}
    result = []
    for ad in data:
        address['ponto'] = str(ad[0][0])
        address['cidade'] = str(ad[1][0])
        address['local'] = str(ad[2][0])
        address['endereco'] = str(ad[3][0])
        address['horario'] = str(ad[4][0])
        address['praca'] = str(ad[6][0])
        result.append(address)
    return result


def save_json_file(data):
    with open('../enderecos.json', 'w') as jp:
        js = json.dumps(data, indent=4, ensure_ascii=False)
        jp.write(js)


if __name__ == '__main__':
    url_donations = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
    driver = create_driver()
    html_content = get_html_content(url_donations, driver)
    adresses = get_donation_points(html_content)
    result = transform_data(adresses)
    save_json_file(result)
