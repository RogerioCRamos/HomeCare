import PySimpleGUI as sg
from Polimorfismos import conexao_bd

def cad_empresas(nome_empresa):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f''' INSERT INTO tb_empresa (nome_empresa)
    VALUE ('{nome_empresa}')
    ''')
    conexao.commit()
    cursor.close()