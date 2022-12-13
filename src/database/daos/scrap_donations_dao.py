from ..mysql_database import MySQLDatabase

TABLE = 'tb_scrap_donations_points'
COLUMNS = '(point, address)'


class ScrapDonationsDAO:
    """ Classe reponsável pelos métodos CRUD dos pontos de doação """

    def __init__(self):
        self.__database = MySQLDatabase(TABLE)

    def save_donations_points(self, points: list):
        """
            Percorre a lista de pontos de doação e os
            converte para a forma esperada pelo método save_all
        """
        values = [(p.point, p.address) for p in points]
        self.__database.save_all(COLUMNS, values)

    def select_all(self):
        """ Retorna uma lista com todos os dados da tabela """
        return self.__database.select_all()

    def close(self):
        """ Encerra a conexão com o banco """
        self.__database.close()
