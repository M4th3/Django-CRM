import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root', #user é root quando não especificado na instalação
    password = 'killkill77'

)
print('testando')
#prepare a cursor object

cursorObj = dataBase.cursor()

#cria um database

cursorObj.execute("CREATE DATABASE crm_db")
print('DB criado com sucesso')