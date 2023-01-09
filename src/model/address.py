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
