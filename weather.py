import PySimpleGUI as sg

layout = [[]]

window = sg.Window("Weather", layout)

while True:
    event, values = windows.read()

    if event == sg.WIN_CLOSED:
        break

window.close()