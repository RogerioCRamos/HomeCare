import PySimpleGUI as sg
from Polimorfismos import *
from FrontNotificar import *
from BackCadEnfermeiras import *

def tela_cad_enfermeiras():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')

    lista_empresas = busca_empresa()

    layout = [[sg.Push(), sg.Text('CADASTRO DE ENFERMEIRAS', auto_size_text=True), sg.Push()],
              [sg.Text()],
              [sg.Text('Nome da Empresa', size=16), sg.Combo(values=lista_empresas, key='-empresas-')],
              [sg.Text('Nome da Enfermeira', size=16), sg.Input(key='-nome_enfermeira-', size=40)],[sg.Text()],[sg.Text()],[sg.Text()],
              [sg.Push(), sg.Text('Login', size=5), sg.Input(key='-login-', size=15),sg.Push()],
              [sg.Push(), sg.Text('Senha', size=5), sg.Input(key='-senha-', size=15), sg.Push()],
              [sg.Text()], [sg.Text()], [sg.Text()],
              [sg.Push(), sg.Button('Confirmar', key='-ok-'), sg.Text("", size=5),sg.Button('Cancelar', key='-cancelar-'), sg.Push()]

    ]

    janela_cad_enfermeira = sg.Window('Home Care', layout, element_justification='l', finalize=True, resizable=True, default_element_size=(100,10), font=(None, 30, "bold"), size=tamanho)


    while True:
        eventos, valores = janela_cad_enfermeira.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == '-ok-':
            codigo = cod_empresa(valores['-empresas-'])
            cad_enfermeiras(valores['-nome_enfermeira-'], codigo, valores['-login-'], valores['-senha-'],)
            tela_erro('Cadastro realizado com sucesso')
            janela_cad_enfermeira.close()
        if eventos == '-cancelar-':
            resposta = tela_notificar('Deseja cancelar o cadastro?')
            if resposta == 'sim':
                janela_cad_enfermeira.close()


tela_cad_enfermeiras()