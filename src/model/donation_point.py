""" Classe modelo para ponto de doação """

class DonationPoint:
    """ Classe modelo para representar um ponto de doação """

    def __init__(self, **kwargs):
        self.point = kwargs.get('point')
        self.city = kwargs.get('city')
        self.place = kwargs.get('place')
        self.address = kwargs.get('address')
        self.opening_hours = kwargs.get('opening_hours')
        self.square = kwargs.get('square')
