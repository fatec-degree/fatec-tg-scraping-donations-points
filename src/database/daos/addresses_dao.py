from datetime import datetime
from ..mysql_database import MySQLDatabase

TABLE = 'tb_addresses'
COLUMNS = '(name, cep, state, city, district,' \
          'street, number, lng, lat, creation_date)'


class AddressesDAO:

    def __init__(self):
        self.__database = MySQLDatabase(TABLE)

    def save_addresses(self, addresses):
        """
            Percorre a lista de endereços e os
            converte para a forma esperada pelo método save_all
        """
        values = [(a.name, a.cep,
                   a.state, a.city,
                   a.district, a.street,
                   a.number, a.lng, a.lat,
                   datetime.now()) for a in addresses]
        self.__database.save_all(COLUMNS, values)

    def delete_inconsistent_data(self):
        """ Deleta do banco todos os dados que
            não seguem um determinado padrão
        """
        where = "LOWER(cep) REGEXP '[a-z]'"
        self.__database.delete(where)

    def close(self):
        """ Encerra a conexão com o banco """
        self.__database.close()
