import PySimpleGUI as sg
import urllib
import urllib.request
from pytube import YouTube
from time import sleep


def log(seg=10):
    sleep(seg)

def Telainici():
    sg.theme('Reddit')
    layout = [[sg.Text('BEM-VINDO!')],
              [sg.Text('Inisira o link:'), sg.Input(key='link')],
              [sg.Text(size=(60,1), key='-OUTPUT-')],
              [sg.Button('Confirmar'), sg.Button('Ajuda'), sg.Button('Sair'), sg.Text('Feito por: Arpanet_01')]
        ]
    return sg.Window('YOUTUBE DOWNLOADER', layout=layout, finalize=True)

def seg():
    sg.theme('Reddit')
    layout = [[sg.Text('Insira no campo 1 o link do vídeo que deseja baixar.')],
              [sg.Text('Clique em confirmar para concluir.')],
              [sg.Text('Aguarde até a mensagem de conclusão e procure o vídeo no seu computador.')],
              [sg.Button('Voltar')]
        ]
    return sg.Window('Ajuda', layout=layout, finalize=True)

janela1, janela2 = Telainici(), None


while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        janela1.close()
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.close()
        break
    if window == janela1 and event == 'Confirmar':
        try:
            link = values['link']
            urllib.request.urlopen(link)
        except:
            window['-OUTPUT-'].update('SITE NÃO ENCONTRADO')
        else:
            try:
                url = values['link']
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()
                video.download()
            except:
                window['-OUTPUT-'].update('CERTIFIQUE-SE DE QUE O LINK É PERTENCENTE AO YOUTUBE')
            else:
                window['-OUTPUT-'].update('VÍDEO BAIXADO! PROCURE NA PASTA DO PROJETO!')
    if window == janela1 and event == 'Ajuda':
        janela1.hide()
        janela2 = seg()
    if window == janela1 and event == 'Sair':
        janela1.hide()
        break
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()






