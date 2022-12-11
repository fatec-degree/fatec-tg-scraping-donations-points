""" Módulo DAO para acesso aos pontos de doação """
import os
from ..mysql_database import MySQLDatabase

HOST = os.environ.get('DB_HOST', 'localhost')
USER = os.environ.get('DB_USER', 'root')
PASSWORD = os.environ.get('DB_PASSWORD', '')
DATABASE = os.environ.get('DB_NAME', 'db_donations')
TABLE = 'tb_donations_points'
COLUMNS = '(point, city, place, address, opening_hours, square)'

class DonationsDAO:
    """ Classe reponsável pelos métodos CRUD dos pontos de doação """

    def __init__(self):
        self.__database = MySQLDatabase(HOST, USER, PASSWORD, DATABASE)

    def save_donations_points(self, points: list):
        """
            Percorre a lista de pontos de doação e os
            converte para a forma esperada pelo método save_all
        """
        values = [(p.point, p.city, p.place, p.address, p.opening_hours, p.square) for p in points]
        self.__database.save_all(TABLE, COLUMNS, values)

    def close(self):
        """ Encerra a conexão com o banco """
        self.__database.close()
