import PySimpleGUI as sg
from Polimorfismos import *
from FrontNotificar import *
from BackCadEmpresa import *

def cad_empresa():
    tamanho = tamanho_tela()

    sg.theme('Bluemono')

    layout = [[sg.Text()],
              [sg.Text('CADASTRO DE EMPRESA', auto_size_text= True)],
              [sg.Text()],
              [sg.Input(key='-nome_empresa-', size=30)],
              [sg.Text()],
              [sg.Button('Confirmar', key= '-ok-'),sg.Text('',size=5), sg.Button('Cancelar', key='-cancelar-')]
]

    janela_cad_empresa = sg.Window(title='Home Care', layout = layout, element_justification= 'c', size= (700,400), finalize= True, resizable= True, font=(None, 30, 'bold'))

    while True:
        eventos, valores = janela_cad_empresa.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == '-ok-':
            try:
                if valores ['-nome_empresa-'] == '':
                    tela_erro('Campo EMPRESA não pode ficar vazio!')
            except Exception as e:
                tela_erro(f'{e}')

        if eventos == ['-ok-']:
            empresa = cad_empresas(valores['-nome_empresa-'])
            tela_erro('Cadastro realizado com sucesso')
            janela_cad_empresa.close()
        if eventos == '-cancelar-':
            resposta = tela_notificar('Deseja cancelar o cadastro?')
            if resposta == 'sim':
                janela_cad_empresa.close()

cad_empresa()