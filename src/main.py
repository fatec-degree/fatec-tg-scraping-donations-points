from model.donation_point import DonationPoint
from database.daos.donations_dao import DonationsDAO
from scraper.donation_scraper import DonationScraper

donation_point_1 = DonationPoint(point='Ponto Carrefour São Caetano',
                                 city='São Bernardo do Campo - SP',
                                 place='Bazar Oneda',
                                 address='Rua Oneda 920, Planalto São Bernardo do Campo - SP',
                                 opening_hours='Das 11h00 às 18h00',
                                 square='São Paulo')

donations_dao = DonationsDAO()
donations_dao.save_donations_points([donation_point_1])
donations_dao.close()
URL_DONATIONS = 'https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/'
scraper = DonationScraper(url=URL_DONATIONS,
                          xpath="//div[@id='searchTextResults']//div[@class='pontocoleta_bloco']",
                          driver_path='resources/chromedriver')
points = scraper.get_donation_points()
scraper.save_json_file()
scraper.quit()
print('SUCCESS')
