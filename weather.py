import PySimpleGUI as sg

# Setting this them will make the them white and match up better with our layout
sg.theme("reddit")

# Seperate these to clean up our second row in the layout
image_col = sg.Column([[sg.Image(key = "-IMAGE-", background_color = "#FFFFFF")]])
info_col = sg.Column([
    [sg.Text("", key = "-LOCATION-", font = "Calibri 30", background_color = "#FF0000", pad = 0, visible = False)],
    [sg.Text("", key = "-TIME-", font = "Calibri 16", background_color = "#000000", text_color = "#FFFFFF", pad = 0, visible = False)],
    [sg.Text("", key = "-TEMP-", font = "Calibri 16", background_color = "#FFFFFF", text_color = "#000000", pad = {0, 10}, justification = "center", visible = False)]
    ])

# Sets up our layout in our window
# Remeber that the layout is in rows, the first row is at the top of the window,
# and the second row is below it
layout = [
    [sg.Input(expand_x = True, key = "-INPUT-"), sg.Button("Submit")],
    [image_col, info_col]
    ]

window = sg.Window("Weather", layout)

while True:
    event, values = windows.read()

    # Handles the case of a user ending the program by pressing the X on the window
    if event == sg.WIN_CLOSED:
        break

    # If the user hits the Submit button, make the information visible
    if evernt == "Submit"
        window["-LOCATION-"].update("test", visible = True)
        window["-TIME-"].update("test", visible = True)
        window["-TEMP-"].update("test", visible = True)
        window["-IMAGE-"].update("symbols/snow.png")

window.close()
