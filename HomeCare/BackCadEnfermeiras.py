import PySimpleGUI as sg
import itertools as it
from Polimorfismos import conexao_bd

def busca_empresa():
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_empresa FROM bd_home_care.tb_empresa")
    retorno = cursor.fetchall()
    lista_empresas = list(it.chain(*retorno))
    return lista_empresas

def cod_empresa(nome_empresa):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT cod_empresa FROM bd_home_care.tb_empresa where nome_empresa = '{nome_empresa}' ")
    retorno = cursor.fetchone()
    return retorno[0]


def cad_enfermeiras(nome_enfermeira, cod_empresa, login, senha):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f''' INSERT INTO tb_cad_enfermeiras (nome_enfermeira, cod_empresa, login, senha)
    VALUES ("{nome_enfermeira}", "{cod_empresa}" , "{login}", "{senha}")''')
    conexao.commit()
    cursor.close()
