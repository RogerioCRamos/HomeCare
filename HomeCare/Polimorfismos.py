#Conexão com o banco de dados
import mysql.connector as sql

def conexao_bd():
    conexao = sql.connect(
        host='localhost',
        user= 'root',
        password='1234',
        database='bd_home_care'
    )

    return conexao

#Presets de banco de dados

#Notificações padrão


#Notificações de erro

#Notificações de erro

