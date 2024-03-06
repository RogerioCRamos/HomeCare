import PySimpleGUI as sg

def tela_notificar(texto):

    sg.theme('BlueMono')

    layout = [[sg.Text(texto, font= (None, 11 , "bold"))],
              [sg.Text()],
              [sg.Button('SIM', key='-sim-', size=(10,2)), sg.Button('NÃO', key='-nao-', size=(10,2))]

              ]

    janela_notificar = sg.Window("HomeCare", layout,  element_justification='c', auto_size_text=True, finalize=True)

    while True:
        eventos , valores = janela_notificar.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == '-sim-':
            resposta = 'sim'
            janela_notificar.close()
            return resposta

        if eventos == '-nao-':
            resposta = 'nao'
            janela_notificar.close()
            return resposta





def tela_erro(texto):

    sg.theme('BlueMono')

    layout = [[sg.Text(texto, font= (None, 11 , "bold"))],
              [sg.Text()],
              [sg.Button('Confirmar', key='-ok-', size=(10,2))]

              ]

    janela_erro = sg.Window("HomeCare", layout,  element_justification='c', auto_size_text=True)

    while True:
        eventos , valores = janela_erro.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == '-ok-':
            janela_erro.close()
