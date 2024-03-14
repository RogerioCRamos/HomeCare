import PySimpleGUI as sg
from Polimorfismos import conexao_bd

def cad_sinais_vitais(glicemia, temperatura, pres_arterial, observacoes):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'''INSERT INTO tb_sinaisvitais (glicemia, temperatura, pres_arterial, observacoes)
    VALUES ("{glicemia}", "{temperatura}", "{pres_arterial}", "{observacoes}")
    ''')
    conexao.commit()
    cursor.close()



