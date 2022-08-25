from time import time
from unicodedata import name
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weather_data(location):
    # We can just get our weather information from the data given by a Google search. When searching for weather
    # on Google, the first part of the URL does not change, so we take that and add on our location to the URL.
    # We also make sure to remove any spaces because URLs cannot have spaces
    url = f"https://www.google.com/search?q=weather+{location.replace(' ', '')}"

    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)

    # Load in the data
    soup = bs(html.text, "html.parser")
    
    # Saving the data from the HTML
    name = soup.find("div", attrs = {"id": "wob_loc"}).text
    time = soup.find("div", attrs = {"id": "wob_dts"}).text
    weather = soup.find("span", attrs = {"id": "wob_dc"}).text
    temperature = soup.find("span", attrs = {"id": "wob_tm"}).text

    return name, time, weather, temperature

# Setting this them will make the them white and match up better with our layout
sg.theme("reddit")

# Separate these to clean up our second row in the layout
image_col = sg.Column([
    [sg.Image("",key = "-IMAGE-", background_color = "#FFFFFF",)]],
    key = "-LEFT-", background_color = "#FFFFFF")
 
info_col = sg.Column([
    [sg.Text("", key = "-LOCATION-", font = "Calibri 30", background_color = "#FF0000", pad = 0, visible = False)],
    [sg.Text("", key = "-TIME-", font = "Calibri 16", background_color = "#000000", text_color = "#FFFFFF", pad = 0, visible = False)],
    [sg.Text("", key = "-TEMP-", font = "Calibri 16", pad = (0,10), background_color = "#FFFFFF", text_color = "#000000", justification = "center", visible = False)]
    ], key = "-RIGHT-", background_color = "#FFFFFF"
    )

# Sets up our layout in our window
# Remember that the layout is in rows, the first row is at the top of the window,
# and the second row is below it
layout = [
    [sg.Input(expand_x = True, key = "-INPUT-"), sg.Button("Submit", button_color = "#000000", border_width = 0)],
    [image_col, info_col]
    ]

window = sg.Window("Weather", layout)

while True:
    event, values = window.read()

    # Handles the case of a user ending the program by pressing the X on the window
    if event == sg.WIN_CLOSED:
        break

    # If the user hits the Submit button, make the information visible
    if event == "Submit":
        name, time, weather, temperature = get_weather_data(values["-INPUT-"])
        window["-LOCATION-"].update(name, visible = True)
        window["-TIME-"].update(time, visible = True)
        window["-TEMP-"].update(temperature, visible = True)
        window["-IMAGE-"].update("symbols/snow.png")

window.close()
