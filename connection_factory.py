import mysql.connector


class ConnectionFactory(object):

    @staticmethod
    def get_connection(host='localhost', user='root', password='123***', db='teste'):
        connection = mysql.connector.connect(
            host=host,
            user=root,
            password=password,
            db=db
        )
        return connection
