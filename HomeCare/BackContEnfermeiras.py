import PySimpleGUI as sg
import itertools as it
from Polimorfismos import conexao_bd

def busca_enfermeiras():
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome_enfermeira FROM bd_home_care.tb_cad_enfermeiras")
    retorno = cursor.fetchall()
    lista_enfermeiras = list(it.chain(*retorno))
    return lista_enfermeiras

def cod_enfermeira(nome_enfermeira):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT cod_enfermeira FROM bd_home_care.tb_cad_enfermeiras where nome_enfermeira = '{nome_enfermeira}' ")
    retorno = cursor.fetchone()
    return retorno[0]


def entrada_enfermeiras(codigo):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'INSERT INTO tb_cont_enfermeira (cod_enfermeira) VALUES ("{codigo}")')
    conexao.commit()
    cursor.close()


def saida_enfermeiras(codigo, observacoes):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'UPDATE tb_cont_enfermeira set dt_saida = CURRENT_TIMESTAMP, observacoes = "{observacoes}" where cod_enfermeira = "{codigo}" and dt_saida IS NULL')
    conexao.commit()
    cursor.close()
