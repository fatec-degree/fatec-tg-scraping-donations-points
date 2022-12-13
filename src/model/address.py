class Address:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.cep = kwargs.get('cep')
        self.state = kwargs.get('state')
        self.city = kwargs.get('city')
        self.district = kwargs.get('district')
        self.street = kwargs.get('street')
        self.number = kwargs.get('number')
        self.lng = kwargs.get('lng')
        self.lat = kwargs.get('lat')

    def __str__(self):
        return f'["name": {self.name}, ' \
               f'"cep": {self.cep}, ' \
               f'"state": {self.state}, ' \
               f'"city": {self.city}, '\
               f'"district": {self.district}, ' \
               f'"street": {self.street}, ' \
               f'"number": {self.number}, ' \
               f'"lng": {self.lng}, ' \
               f'"lat": {self.lat}]'
