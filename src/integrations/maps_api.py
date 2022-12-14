import googlemaps


class MapsAPI:

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__client = googlemaps.Client(key=self.__api_key)

    def get_complete_address(self, address):
        """ Retorna um endereço formatado """
        result = self.__client.geocode(address)[0]
        address_components = result.get('address_components')
        geometry = result.get('geometry')
        complete_address = {
            'number': address_components[0].get('long_name'),
            'street': address_components[1].get('long_name'),
            'district': address_components[2].get('long_name'),
            'city': address_components[3].get('long_name'),
            'state': address_components[4].get('long_name'),
            'cep': str(address_components[6].
                       get('long_name')).replace('-', ''),
            'lat': geometry.get('location').get('lat'),
            'lng': geometry.get('location').get('lng')
        }
        return complete_address
