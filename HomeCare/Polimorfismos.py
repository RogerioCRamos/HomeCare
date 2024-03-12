#Conexão com o banco de dados
import mysql.connector as sql
import itertools as it

def conexao_bd():

    conexao = sql.connect(
        host='localhost',
        user= 'root',
        password='1234',
        database='bd_home_care'
    )

    return conexao

def tamanho_tela():

    tamanho = (1920,1080)
    return tamanho


def posicao_data():

    posicao = (1580,155)
    return posicao


def converter_data(data):

    inversao = data.split('/')
    inversao = inversao[::-1]
    inversao = '-'.join(inversao)
    return inversao

def conferir_codigo(codigo):

    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'SELECT cod_material FROM tb_material where cod_material = "{codigo}"')
    retorno = cursor.fetchall()
    if retorno != []:
        resultado = 1
        cursor.execute(f'SELECT nome_material FROM tb_material where cod_material = "{codigo}"')
        material = cursor.fetchall()
        material = list(it.chain(*material))
        material = "".join(material)
    else:
        resultado = 0
        material = ""

    return resultado, material
