""" Módulo principal do sistema """
import os
from database.daos.scrap_donations_dao import ScrapDonationsDAO
from model.donation_point import DonationPoint
from scraper.donation_scraper import DonationScraper
from integrations.maps_api import MapsAPI
from model.address import Address
from integrations.donations_api import DonationsAPI

API_KEY = os.environ.get('MAPS_API_KEY')
URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
DONATIONS_URL_API = os.environ.get('ADDRESS_API_URL_LOCAL')
if os.environ.get('ENVIRONMENT') == 'prd':
    DONATIONS_URL_API = os.environ.get('ADDRESS_API_URL_PRD')

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
# TODO - ir para o próximo passo direto
# sem ter que consultar os dados no banco novamente
scraping_donations_points = [(p[1], p[2]) for p in donations_dao.select_all()]
maps = MapsAPI(API_KEY)
complete_ads = []
for s in scraping_donations_points:
    try:
        complete_ads.append(maps.get_complete_address(s[1]))
    except Exception:
        continue

# Criar uma lista de objetos Address a partir dos endereços completos
address_models = []
for i in range(0, len(complete_ads)):
    address_models.append(Address(
        name=scraping_donations_points[i][0],
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
