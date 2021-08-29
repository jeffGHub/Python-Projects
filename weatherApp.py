import tkinter as tk
from tkinter import font
import requests


HEIGHT = 600
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

# 4992ec6b5573166b6f9e1704ac1b894f
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        temp = weather['main']['temp']
        desc = weather['weather'][0]['description']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '4992ec6b5573166b6f9e1704ac1b894f'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    param = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=param)
    weather = response.json()

    label['text'] = format_response(weather)

    print(weather['name'])
    print(weather['main']['temp'])
    print(weather['weather'][0]['description'])




root = tk.Tk()
root.title('My Weather App')
root.iconbitmap('favicon.ico')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#FFE37A', bd=2)
frame.place(relx=.5, rely=.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, bg='#eee', font=('Courier', ))
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=.7, relheight=1, relwidth=.3)

lower_frame = tk.Frame(root, bg='#FFE37A', bd=2)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), bg='#eee', anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()