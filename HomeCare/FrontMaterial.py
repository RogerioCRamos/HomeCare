import PySimpleGUI as sg
import itertools as it
from Polimorfismos import *
from FrontNotificar import *
from BackMaterial import *
import locale
from datetime import datetime, date

# Configura o locale para português (Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def tela_cad_material():

    tamanho = tamanho_tela()
    posicao = posicao_data()

    sg.theme('Bluemono')

    layout = [[sg.Push(), sg.Text('CADASTRO DE MATERIAL', auto_size_text=True), sg.Push()],
              [sg.Text()],[sg.Text()],[sg.Text()],[sg.Text()],
              [sg.Text('Codigo: ',), sg.Input(key='-codigo-', size=10),sg.Push(),sg.Text('Data de recebimento: '), sg.Input(key='-data-', disabled=True, size=12),sg.CalendarButton('Data', key='-botaodata-', target='-data-', enable_events=True , format='%d/%m/%Y', locale='pt_BR.UTF-8', size=(5,1), font=(None, 20, 'bold'), location=(posicao)), sg.Push()],
              [sg.Text()],[sg.Text()],
              [sg.Text('Nome do Material: '), sg.Input(key='-material-')],
              [sg.Text()],
              [sg.Text('Numero do lote: '), sg.Input(key='-lote-', size=10),sg.Push(),
              sg.Text('Quantidade: '), sg.Input(key='-quantidade-', size=10), sg.Push(),
              sg.Text('Unidade de medida: '), sg.Input(key='-unmedida-', size=10), sg.Push()],
              [sg.Text()],[sg.Text()],[sg.Text()],[sg.Text()],
              [sg.Push(),sg.Button('Confirmar', key='-ok-'), sg.Text("",size=5), sg.Button('Cancelar', key='-cancelar-'), sg.Push()]
              ]

    janela_cad_material = sg.Window('Home Care', layout, element_justification='l', finalize=True, resizable=True, default_element_size=(100,10), font=(None, 30, "bold"), size=tamanho)


    while True:
        eventos, valores = janela_cad_material.read()


        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == '-cancelar-':
            resposta = tela_notificar("Deseja cancelar o cadastro do item?")
            if resposta == 'sim':
                janela_cad_material.close()

        if eventos == '-ok-':
            try:
                if valores['-codigo-'] == '':
                    tela_erro("Campo CÓDIGO não pode ficar vazio")
                elif valores['-data-'] == '':
                    tela_erro("Campo DATA DE RECEBIMENTO não pode ficar vazio")
                elif valores['-material-'] == '':
                    tela_erro("Campo NOME DO MATERIAL não pode ficar vazio")
                elif valores['-lote-'] == '':
                    tela_erro("Campo NUMERO DO LOTE não pode ficar vazio")
                elif valores['-quantidade-'] == '':
                    tela_erro("Campo QUANTIDADE não pode ficar vazio")
                elif valores['-unmedida-'] == '':
                    tela_erro("Campo UNIDADE DE MEDIDA não pode ficar vazio")
                elif not valores['-codigo-'].isdigit():
                    raise ValueError(f"Campo CÓDIGO aceita somente numeros")
                elif not valores['-quantidade-'].isdigit():
                    raise ValueError(f"Campo QUANTIDADE aceita somente numeros")

                else:
                    data_recebimento_str = converter_data(valores['-data-'])
                    data_recebimento = datetime.strptime(data_recebimento_str, '%Y-%m-%d').date()
                    if data_recebimento > date.today():
                        tela_erro("Data de recebimento não pode ser maior que a data de hoje")
                    else:
                        cad_materiais(valores['-codigo-'], valores['-material-'], valores['-lote-'], valores['-quantidade-'],valores['-unmedida-'], data_recebimento)
                        tela_erro(f'Item {valores['-material-']} cadastrado com sucesso!!')
            except Exception as e:
                tela_erro(f'{e}')


def tela_uso_material():

    tamanho = tamanho_tela()

    sg.theme('Bluemono')

    layout = [[sg.Push(), sg.Text('CADASTRO DE USO DE MATERIAL', auto_size_text=True), sg.Push()],
              [sg.Text()], [sg.Text()], [sg.Text()], [sg.Text()],
              [sg.Text('Codigo: ', ), sg.Input(key='-codigo-', size=10),sg.Button("Pesquisar", key='-pesquisar-', font=(None, 20, 'bold')),sg.Push()],
              [sg.Text()], [sg.Text()],
              [sg.Text('Nome do Material: '), sg.Input(key='-material-', disabled=True)],
              [sg.Text()],
              [sg.Text('Quantidade utilizada: '), sg.Input(key='-quantidade-', size=10), sg.Push()],
              [sg.Text()], [sg.Text()], [sg.Text()], [sg.Text()],
              [sg.Push(), sg.Button('Confirmar', key='-ok-'), sg.Text("", size=5),
               sg.Button('Cancelar', key='-cancelar-'), sg.Push()]
              ]

    janela_cad_material = sg.Window('Home Care', layout, element_justification='l', finalize=True, resizable=True,
                                    default_element_size=(100, 10), font=(None, 30, "bold"), size=tamanho)

    while True:
        eventos, valores = janela_cad_material.read()

        if eventos == sg.WINDOW_CLOSED:
            break

        if eventos == '-cancelar-':
            resposta = tela_notificar("Deseja cancelar o cadastro do item?")
            if resposta == 'sim':
                janela_cad_material.close()

        if eventos == '-pesquisar-':
            codigo_conferido, material = conferir_codigo(valores['-codigo-'])
            if codigo_conferido == 0:
                janela_cad_material['-material-'].update(material)
                tela_erro("Codigo não existe")
            else:
                consulta_quantidade_material(valores['-codigo-'], material)
                janela_cad_material['-material-'].update(material)

        if eventos == '-ok-':
            try:
                if valores['-material-'] == '':
                    tela_erro("Campo NOME DO MATERIAL não pode ficar vazio! Preencha o campo CÓDIGO com um número válido e clique no botão PESQUISAR")
                elif valores['-quantidade-'] == '':
                    tela_erro("Campo QUANTIDADE UTILIZADA não pode ficar vazio")
                elif not valores['-quantidade-'].isdigit():
                    raise ValueError(f"Campo QUANTIDADE UTILIZADA aceita somente numeros")
                else:
                    quantidade_atual = consulta_quantidade_material(valores['-codigo-'], material)
                    if int(valores['-quantidade-']) > quantidade_atual:
                        tela_erro("Valor informado maior que quantidade em estoque")
                    else:
                        cad_uso_material(material, valores['-quantidade-'])


            except Exception as e:
                tela_erro(f'{e}')




tela_cad_material()









