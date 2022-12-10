""" Web Scraping de um site de pontos de doação de agasalhos """

import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by


def create_driver():
    """ Cria um webdriver a partir do arquivo definido na pasta resources """
    option = Options()
    option.headless = True
    return webdriver.Chrome(executable_path='resources/chromedriver', options=option)


def get_html_content(url):
    """ Extrai o HTML da página especificada no parâmetro url """
    driver = create_driver()
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements(by=by.By.XPATH, value="//div[@class='pontocoleta_bloco']")
    html = [e.get_attribute('outerHTML') for e in elements]
    driver.quit()
    return html


def get_donation_points(html):
    """ Extrai do html os pontos de doação """
    soup = [BeautifulSoup(div, 'html.parser') for div in html]
    donation_points = []
    for tag in soup:
        spans = tag.find_all('span')
        donation_points.append([span.contents for span in spans])
    return donation_points


def remove_title(value: str):
    """ Remove o título dos dados """
    try:
        return value.split(':', 1)[1].strip()
    except IndexError:
        return value.strip()


def transform_data(values):
    """ Transforma os dados em um dicionário próprio """
    data_transformed = []
    for value in values:
        data_transformed.append({
            'ponto': remove_title(str(value[0][0])),
            'cidade': remove_title(str(value[1][0])),
            'local': remove_title(str(value[2][0])),
            'endereco': remove_title(str(value[3][0])),
            'horario': remove_title(str(value[4][0])),
            'praca': remove_title(str(value[6][0]))
        })
    return data_transformed


def save_json_file(file):
    """ Salva os dados em um arquivo json """
    with open('../enderecos.json', 'w', encoding='utf-8') as json_dump:
        json_file = json.dumps(file, indent=4, ensure_ascii=False)
        json_dump.write(json_file)


if __name__ == '__main__':
    URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
    data = get_html_content(URL_DONATIONS)
    data = get_donation_points(data)
    data = transform_data(data)
    save_json_file(data)
