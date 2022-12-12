""" Módulo principal do sistema """
from database.daos.donations_dao import DonationsDAO
from model.donation_point import DonationPoint
from scraper.donation_scraper import DonationScraper

URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
scraper = DonationScraper(url=URL_DONATIONS,
                          xpath="//div[@id='searchTextResults']//div[@class='pontocoleta_bloco']",
                          driver_path='resources/chromedriver')
points = scraper.get_donation_points()
donations_points = [DonationPoint(point=p.get('point'),
                                  address=p.get('address')) for p in points]
scraper.quit()
donations_dao = DonationsDAO()
donations_dao.save_donations_points(donations_points)
donations_dao.close()
print('SUCCESS')
