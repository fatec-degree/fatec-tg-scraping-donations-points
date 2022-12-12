""" Web Scraping de um site de pontos de doação de agasalhos """

import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by


class DonationScraper:
    """ Classe que faz o processo de scraping do site de doações """

    def __init__(self, url, xpath, driver_path) -> None:
        self.__url = url
        self.__xpath = xpath
        self.__driver_path = driver_path
        self.__driver = self.__create_driver()

    def __create_driver(self):
        """ Cria um webdriver a partir do arquivo passado como parametro """
        option = Options()
        option.headless = True
        return webdriver.Chrome(executable_path=self.__driver_path, options=option)


    def __get_html_content(self):
        """ Extrai o HTML da página especificada no parâmetro url """
        self.__driver.get(self.__url)
        time.sleep(5)
        xpath = self.__xpath
        elements = self.__driver.find_elements(by=by.By.XPATH, value=xpath)
        html = [e.get_attribute('outerHTML') for e in elements]
        return html

    def __remove_title(self, value):
        """ Remove o título dos dados """
        try:
            return value.split(':', 1)[1].strip()
        except IndexError:
            return value.strip()

    def __transform_data(self, values):
        """ Transforma os dados em um dicionário próprio """
        data_transformed = []
        for value in values:
            data_transformed.append({
                'point': self.__remove_title(value[0][0]),
                'city': self.__remove_title(value[1][0]),
                'place': self.__remove_title(value[2][0]),
                'address': self.__remove_title(value[3][0]),
                'opening_hours': self.__remove_title(value[4][0]),
                'square': self.__remove_title(value[6][0])
            })
        return data_transformed

    def quit(self):
        """ Fecha a conexão com o webdriver """
        self.__driver.quit()

    def get_donation_points(self):
        """ Extrai do html os pontos de doação """
        html = self.__get_html_content()
        soup = [BeautifulSoup(div, 'html.parser') for div in html]
        donation_points = []
        for tag in soup:
            spans = tag.find_all('span')
            donation_points.append([span.contents for span in spans])
        return self.__transform_data(donation_points)

    def save_json_file(self):
        """ Salva os dados em um arquivo json """
        file = self.get_donation_points()
        with open('enderecos.json', 'w', encoding='utf-8') as json_dump:
            json_file = json.dumps(file, indent=4, ensure_ascii=False)
            json_dump.write(json_file)
