import tkinter as tk
import requests

class Gui:
    def __init__(self,key,location,bg,fg,font,font_size):
        self.root = tk.Tk(className='Weather')
        self.root.geometry('500x220')
        self.root.configure(bg=bg)

        # Theme
        self.bg = bg
        self.fg = fg
        self.font = font
        self.font_size = font_size
        
        # Weather
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.url = self.base_url + 'appid=' + key + '&q=' + location
        self.response = requests.get(self.url).json()

        # Get temps
        self.temp = ' Temperature: ' + str(int(self.response['main']['temp'])-273)
        self.clouds = '󰅟 Clouds: ' + str(self.response['weather'][0]['description'])
        self.speed = ' Speed: ' + str(int(self.response['wind']['speed'])-1.6)
        
        self.new_label(' ' + location)
        self.new_label(self.temp + '')
        self.new_label(self.clouds)
        self.new_label(self.speed)
        
    def new_label(self, text):
        self.new = tk.Label(text=text, background=self.bg, foreground=self.fg, font=(self.font, self.font_size), anchor='center')
        self.new.pack(side='top', fill='both', pady=5)


    def run(self):
        self.root.mainloop()