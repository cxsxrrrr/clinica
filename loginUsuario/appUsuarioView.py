# paquetes
from administracion.admin import admin

from administracion.admin import admin
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class UsuarioScreen(Screen):
    def __init__(self, **kwargs):
        super(UsuarioScreen , self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        font="./fuentes/coolvetica.otf"

        self.button = Button(text="Cerrar sesion", on_press=self.switch_to_home, font_size=25,font_name=font)
        self.add_widget(self.button)

        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17

    #VOLVER
    def switch_to_home(self, instance):
        self.manager.current = 'login'

        
