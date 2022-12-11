""" Módulo de conexão com banco de dados MySQL """
import mysql.connector


class MySQLDatabase:
    """ Classe que faz a conexão com o banco e realiza operações CRUD """

    def __init__(self, host, user, password, database):
        self.__conn = self.__connect(host, user, password, database)
        self.__cursor = self.__conn.cursor()

    def __connect(self, host, user, password, database):
        """ Cria um objeto de conexão com o MySQL """
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)

    def __is_connected(self) -> bool:
        """ Verifica se ainda há conexão com o banco """
        return self.__conn.is_connected()

    def __str_values(self, size):
        """ Cria uma string com tamanho n para fazer o insert no banco """
        values = ''
        while size > 1:
            values += '%s, '
            size -= 1
        values += '%s'
        return values

    def save_all(self, table, columns: str, values):
        """ Salva n registros no banco de dados """
        if self.__is_connected():
            sql = "INSERT INTO " + table + " " + str(columns) + \
                  " VALUES (" + self.__str_values(columns.count(',') + 1) + ")"
            self.__cursor.executemany(sql, values)
            self.__conn.commit()
            self.__cursor.close()

    def close(self):
        """ Encerra a conexão com o banco """
        self.__conn.close()
