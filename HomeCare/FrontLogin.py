import PySimpleGUI as sg
from BackLogin import *
from Polimorfismos import *
from FrontNotiicar import tela_notificar

def tela_login():

    sg.theme('Bluemono')

    layout = [[sg.Text("")],[sg.Text("Login",font= (None, 11 , "bold"), size=6), sg.Input(key="-login-")],
              [sg.Text("Senha",font= (None, 11 , "bold"), size=6), sg.Input(key="-senha-", password_char='*')],
              [sg.Text("")],
              [sg.Push(),sg.Button("Acessar", size=(10,2), key='-acessar-',font= (None, 11 , "bold")), sg.Push(), sg.Button("Cancelar", size=(10,2), key='-cancelar-', font= (None, 11 , "bold")),sg.Push()]
    ]

    janela_login = sg.Window("Home Care", layout, size=(300, 170), element_justification='c', finalize=True, resizable=False)


    while True:
        eventos, valores = janela_login.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == '-acessar-':
            validar_login(user=valores['-login-'], senha=valores['-senha-'])

        if eventos == '-cancelar-':
            resposta = tela_notificar('Quer cancelar o Login?')
            if resposta == 'sim':
                janela_login.close()
            else:
                pass

tela_login()