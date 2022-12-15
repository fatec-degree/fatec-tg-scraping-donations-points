""" Módulo principal do sistema """
import os
from database.daos.scrap_donations_dao import ScrapDonationsDAO
from database.daos.addresses_dao import AddressesDAO
from model.donation_point import DonationPoint
from scraper.donation_scraper import DonationScraper
from integrations.maps_api import MapsAPI
from model.address import Address


API_KEY = os.environ.get('MAPS_API_KEY')
URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'

# Scraping dos dados
scraper = DonationScraper(url=URL_DONATIONS,
                          xpath="//div[@id='searchTextResults']//\
                          div[@class='pontocoleta_bloco']",
                          driver_path='resources/chromedriver')
points = scraper.get_donation_points()
scraper.quit()
donations_points = [DonationPoint(point=p.get('point'),
                                  address=p.get('address')) for p in points]

# Salva os dados do scraping no banco
donations_dao = ScrapDonationsDAO()
donations_dao.save_donations_points(donations_points)

# Busca os dados do scraping do banco e faz requisições a API do Google Maps
# para buscar o endereço completo e organizado
scraping_donations_points = [(p[1], p[2]) for p in donations_dao.select_all()]
maps = MapsAPI(API_KEY)
complete_ads = []
for s in scraping_donations_points:
    try:
        complete_ads.append(maps.get_complete_address(s[1]))
    except Exception:
        continue

# Criar uma lista de objetos Address a partir dos endereços completos
adress_models = []
for i in range(0, len(complete_ads)):
    adress_models.append(Address(
        name=scraping_donations_points[i][0],
        cep=complete_ads[i].get('cep'),
        district=complete_ads[i].get('district'),
        street=complete_ads[i].get('street'),
        number=complete_ads[i].get('number'),
        lng=complete_ads[i].get('lng'),
        lat=complete_ads[i].get('lat'),
        city=complete_ads[i].get('city'),
        state=complete_ads[i].get('state')))

# Salva os endereços completos no banco
addresses_dao = AddressesDAO()
addresses_dao.save_addresses(adress_models)

# Remove dados inconsistentes
addresses_dao.delete_inconsistent_data()

# Finaliza o programa
addresses_dao.close()
donations_dao.close()
print('SUCCESS')
