import PySimpleGUI as sg
from Polimorfismos import conexao_bd

def cad_visita_medica(nome_medico, cod_especialidade, observacoes):
    conexao = conexao_bd()
    cursor = conexao.cursor()

    codigo_visita = gerar_codigo_visita()
    cursor.execute(f'''INSERT INTO tb_visitamedica (cod_visita, nome_medico, cod_especialidade, observacoes)
                   VALUES ('{codigo_visita}', '{nome_medico}', '{cod_especialidade}', '{observacoes}')
''')
    conexao.commit()
    cursor.close()
    print(f'chamado {codigo_visita} cadastrado com sucesso')

def buscar_visita_medica(cod_visita):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f"select  observacoes from tb_visitamedica where cod_visita = '{cod_visita}'")
    retorno = cursor.fetchone()
    cursor.close()

    for dados in retorno:
        resultado = dados
        print(resultado)


def editar_visita_medica(cod_visita, observacoes):
    conexao = conexao_bd()
    cursor = conexao.cursor()
    cursor.execute(f'''UPDATE tb_visitamedica
    SET observacoes = "{observacoes}", dt_saida = CURRENT_TIMESTAMP
    where cod_visita = "{cod_visita}"     
    ''')
    conexao.commit()
    cursor.close()


def gerar_codigo_visita():

    conexao = conexao_bd()
    busca_codigo_anterior = conexao.cursor()
    busca_codigo_anterior.execute('SELECT max(cod_visita) FROM tb_visitamedica;')
    retorno = busca_codigo_anterior.fetchone()
    busca_codigo_anterior.close()
    if retorno[0] == None:
       codigo = 1
    else:
        codigo = retorno[0] +1
    return codigo

