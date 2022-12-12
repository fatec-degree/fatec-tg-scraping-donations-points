""" Classe modelo para ponto de doação """


class DonationPoint:
    """ Classe modelo para representar um ponto de doação """

    def __init__(self, **kwargs):
        self.point = kwargs.get('point')
        self.address = kwargs.get('address')
