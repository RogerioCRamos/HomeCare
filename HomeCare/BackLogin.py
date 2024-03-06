from Polimorfismos import conexao_bd
from FrontNotiicar import tela_erro
def validar_login(user,senha):

    conexao = conexao_bd() #coloca a variável que retorna de "conexão_bd()" dentro da variável "conexão"
    cursor = conexao.cursor() #cria um cursor a partir da variável "conexão" para percorrer o banco
    cursor.execute(f"SELECT usuario,senha, dt_desativacao, nome_usuario FROM tb_usuario where usuario = '{user}'") #faz o cursor executar uma consulta no BD

    retorno = cursor.fetchone() #retorno da consulta no banco de dados
    cursor.close() #fechamento do cursor

    #validação se o usuario está correto
    if retorno is None:
        tela_erro('usuario incorreto')

    else:
        # validação se o usuario está ativado ou desativado
        if retorno[2] is None:

            # validação de senha
            if retorno[1] != senha:
                tela_erro('senha incorreta')
            else:
                print(f'está logado, seja bem vindo(a) {retorno[3]}')

        else:
            tela_erro('usuario desativado')





