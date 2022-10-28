import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from bs4 import BeautifulSoup


def create_driver():
    option = Options()
    option.headless = True
    return webdriver.Chrome(executable_path='resources/chromedriver', options=option)


def get_html_content(url, web_driver):
    web_driver.get(url)
    time.sleep(5)
    elements = web_driver.find_elements(by=by.By.XPATH, value="//div[@class='pontocoleta_bloco']")
    html = [e.get_attribute('outerHTML') for e in elements]
    web_driver.quit()
    return html


def get_donation_points(html):
    soup = [BeautifulSoup(div, 'html.parser') for div in html]
    donation_points = []
    for tag in soup:
        spans = tag.find_all('span')
        donation_points.append([span.contents for span in spans])
    return donation_points


def transform_data(data):
    address = {}
    data_transformed = []
    for value in data:
        address['ponto'] = str(value[0][0])
        address['cidade'] = str(value[1][0])
        address['local'] = str(value[2][0])
        address['endereco'] = str(value[3][0])
        address['horario'] = str(value[4][0])
        address['praca'] = str(value[6][0])
        data_transformed.append(address)
    return data_transformed


def save_json_file(data):
    with open('../enderecos.json', 'w', encoding='utf-8') as json_dump:
        json_file = json.dumps(data, indent=4, ensure_ascii=False)
        json_dump.write(json_file)


if __name__ == '__main__':
    URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
    driver = create_driver()
    html_content = get_html_content(URL_DONATIONS, driver)
    adresses = get_donation_points(html_content)
    result = transform_data(adresses)
    save_json_file(result)
