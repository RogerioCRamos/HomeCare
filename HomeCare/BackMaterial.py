import PySimpleGUI as sg
import itertools as it
from Polimorfismos import conexao_bd
from FrontNotificar import *

def cad_materiais(codigo, material, lote, quantidade, un_medida, data_recebimento):
    #Conexão com o banco de dados
    conexao = conexao_bd()
    #Cursos para procurar os itens no banco de dados
    cursor = conexao.cursor()
    #Executar o cursor
    cursor.execute(f'''INSERT INTO tb_material (cod_material, nome_material, num_lote, quantidade, un_medida, dt_recebimento) 
    VALUES ("{codigo}", "{material}", "{lote}", "{quantidade}", "{un_medida}", "{data_recebimento}")
    ''')
    conexao.commit()
    cursor.close()

def consulta_quantidade_material(codigo, material):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'SELECT quantidade FROM tb_material WHERE cod_material = "{codigo}" AND nome_material = "{material}" ')
    retorno = cursor.fetchall()
    lista_material = list(it.chain(*retorno))
    lista_material = sum(lista_material)
    print(lista_material)
    cursor.close()
    return lista_material

def cad_uso_material(material, qt_utilizada):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'SELECT cod_material , nome_material, un_medida FROM tb_material WHERE nome_material = "{material}"')
    retorno = cursor.fetchone()

    if retorno is not None:
        cursor.fetchall()
        cursor.execute(f'''INSERT INTO tb_usomaterial (cod_material, quantidade_utilizada, dt_uso) 
        VALUES ("{retorno[0]}","{qt_utilizada}", CURRENT_TIMESTAMP())
        ''')
        conexao.commit()
        tela_erro(f'Cadastro de utilização de {qt_utilizada} {retorno[2]}(s) de {material} realizado com sucesso')
        cursor.close()
    else:
        tela_erro('Material informado incorretamente!')


