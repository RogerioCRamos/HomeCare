import PySimpleGUI as sg
from Polimorfismos import *
from FrontNotificar import *
from BackContEnfermeiras import *

def tela_entrada_enfermeira():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')

    lista_enfermeiras = busca_enfermeiras()

    layout = [[sg.Push(), sg.Text('CONTROLE DE ENFERMEIRAS (ENTRADA)', auto_size_text=True), sg.Push()],
              [sg.Text()],[sg.Text()],[sg.Text()],
              [sg.Text('Selecione a enfermeira')],
              [sg.Combo(values=lista_enfermeiras, key='-enfermeiras-')],
              [sg.Text()], [sg.Text()], [sg.Text()],
              [sg.Push(), sg.Button('Confirmar', key='-ok-'), sg.Text("", size=5),sg.Button('Cancelar', key='-cancelar-'), sg.Push()]

    ]

    janela_entrada_enfermeiras = sg.Window('Home Care', layout, element_justification='c', finalize=True, resizable=True, default_element_size=(100,10), font=(None, 30, "bold"), size=tamanho)


    while True:
        eventos, valores = janela_entrada_enfermeiras.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == '-ok-':
            codigo = cod_enfermeira(valores['-enfermeiras-'])
            entrada_enfermeiras(codigo)
            tela_erro('Entrada realizada com sucesso')
            janela_entrada_enfermeiras.close()

        if eventos == '-cancelar-':
            resposta = tela_notificar('Deseja cancelar a entrada?')
            if resposta == 'sim':
                janela_entrada_enfermeiras.close()

tela_entrada_enfermeira()

'''def tela_saida_enfermeira():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')'''



'''def tela_controle_manual():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')'''