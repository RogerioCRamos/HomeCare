import PySimpleGUI as sg
from Polimorfismos import *
from FrontNotificar import *
from BackCadSinaisVitais import *

def tela_cad_sinais_vitais():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')

    layout = [[sg.Text()],
             [sg.Text('CADASTRO DE SINAIS VITAIS', auto_size_text= True)],
             [sg.Text()],
             [sg.Text('Glicemia'), sg.Input(key='-glicemia-', size=7), sg.Text('Temperatura'), sg.Input(key='-temperatura-', size=7), sg.Text('Pressão Arterial'), sg.Input(key='-pres_arterial-', size=7)],
             [sg.Text()],
             [sg.Text('Observações')],
             [sg.Multiline(key='-observacoes-', size=(50,5))],
             [sg.Text()],
             [sg.Button('Confirmar', key='-ok-'), sg.Text(size=5), sg.Button('Cancelar', key='-cancelar-')]
    ]
    janela_cad_sinais_vitais = sg.Window(title='Home Care', layout= layout, element_justification='c', size= tamanho, finalize= True, resizable= True, font=(None, 30, 'bold'))

    while True:
        eventos, valores = janela_cad_sinais_vitais.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == '-ok-':
            try:
                if valores ['-pres_arterial-'] != ' / ':
                    tela_erro('O campo pressão arterial deve ser preenchido com uma barra (/) no meio')
            except Exception as e:
                tela_erro(f'{e}')

        if eventos == ['-ok-']:
           sinais_vitais = cad_sinais_vitais(valores['-glicemia-'], valores['-temperatura-'], valores['-pres_arterial-'], valores['-observacoes-'])
           tela_erro('Cadastro realizado com sucesso!')
           janela_cad_sinais_vitais.close()

        if eventos == '-cancelar-':
           resposta = tela_notificar('Deseja cancelar o cadastro?')
           if resposta == 'sim':
               janela_cad_sinais_vitais.close()


tela_cad_sinais_vitais()