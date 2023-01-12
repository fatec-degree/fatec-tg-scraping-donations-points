""" Módulo principal do sistema """
import os
from scraper.donation_scraper import DonationScraper
from database.daos.scrap_donations_dao import ScrapDonationsDAO
from model.donation_point import DonationPoint
from model.address import Address
from integrations.maps_api import MapsAPI
from integrations.donations_api import DonationsAPI

API_KEY = os.environ.get('MAPS_API_KEY')
URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
DONATIONS_URL_API = os.environ.get('ADDRESS_API_URL')

# Scraping dos dados
scraper = DonationScraper(url=URL_DONATIONS,
                          xpath="//div[@id='searchTextResults']//\
                          div[@class='pontocoleta_bloco']")
points = scraper.get_donation_points()
scraper.quit()
donations_points = [DonationPoint(point=p.get('point'),
                                  address=p.get('address')) for p in points]

# Salva os dados do scraping no banco
donations_dao = ScrapDonationsDAO()
donations_dao.save_donations_points(donations_points)

# Itera os dados extraídos no processo de scraping e faz requisições a 
# API do Google Maps para buscar o endereço completo e organizado
maps = MapsAPI(API_KEY)
complete_ads = []
for d in donations_points:
    try:
        complete_ads.append(maps.get_complete_address(d.address))
    except Exception:
        continue

# Cria uma lista de objetos Address a partir dos endereços completos
address_models = []
for i in range(0, len(complete_ads)):
    address_models.append(Address(
        name=donations_points[i].point,
        cep=complete_ads[i].get('cep'),
        district=complete_ads[i].get('district'),
        street=complete_ads[i].get('street'),
        number=complete_ads[i].get('number'),
        lng=complete_ads[i].get('lng'),
        lat=complete_ads[i].get('lat'),
        city=complete_ads[i].get('city'),
        state=complete_ads[i].get('state')))

# Remove dados inconsistentes
for ad in address_models:
    if not ad.cep.isnumeric():
        address_models.remove(ad)

# Salva os endereços completos no banco através da API
donations_api = DonationsAPI(DONATIONS_URL_API)
for ad in address_models:
    donations_api.save_address(ad)

# Finaliza o programa
donations_dao.close()
print('SUCCESS')
