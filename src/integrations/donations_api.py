import requests
import json

from model.address import Address


class DonationsAPI:

    def __init__(self, base_url) -> None:
        self.__base_url = base_url
        self.__headers = {'Content-Type': 'application/json'}

    def __convert_to_json(self, object):
        return json.dumps(object.__dict__)

    def save_address(self, address):
        url = f'{self.__base_url}/donations-points'
        body = self.__convert_to_json(address)
        response = requests.post(url=url, data=body, headers=self.__headers)
        return response.json()
