from model.donation_point import DonationPoint
from database.daos.donations_dao import DonationsDAO

donation_point_1 = DonationPoint(point='Ponto Carrefour São Caetano',
                                 city='São Bernardo do Campo - SP',
                                 place='Bazar Oneda',
                                 address='Rua Oneda 920, Planalto São Bernardo do Campo - SP',
                                 opening_hours='Das 11h00 às 18h00',
                                 square='São Paulo')

donation_point_2 = DonationPoint(point='Ponto Carrefour São Caetano',
                                 city='São Bernardo do Campo - SP',
                                 place='Bazar Oneda',
                                 address='Rua Oneda 920, Planalto São Bernardo do Campo - SP',
                                 opening_hours='Das 11h00 às 18h00',
                                 square='São Paulo')

donations_dao = DonationsDAO()
donations_dao.save_donations_points([donation_point_1])
donations_dao.close()
print('SUCCESS')
