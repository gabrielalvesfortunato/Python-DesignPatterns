from connection_factory import ConnectionFactory


try:
    connection = ConnectionFactory.get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cursor')

    for linha in cursor:
        print(linha)

except ConnectionError:
    raise ConnectionError("Não foi possível se conectar ao banco de dados.")
finally:
    connection.close()
