#packages
import sys
sys.path.append('../clinica')
from administracion.admin import admin
# kivy imports
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup

#sql imports
import sqlite3

class updatePassword(Screen):

    def __init__(self, **kwargs):
        super(updatePassword, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        # VENTANA
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        #FUENTE A USAR

        font="./fuentes/coolvetica.otf"

        # Create labels for username and password
        self.username_label = Label(text="Contraseña antigua:", font_name=font, font_size=25)
        self.password_label = Label(text="Contraseña nueva:", font_name=font, font_size=25)

        # Create text input fields for username and password
        self.password1 = TextInput(password=True, hint_text="last password", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.password2 = TextInput(password=True, multiline=False, hint_text="new password", font_name=font, font_size=20, padding=[5, 15, 0, 0])

        # Create a login button
        self.cambio = Button(text="Cambiar", on_press=self.on_cambio_press, font_name=font, font_size=25)
    
        # Add widgets to the layout with relative positioning
        self.add_widget(self.username_label)
        self.add_widget(self.password_label)
        self.add_widget(self.password1)
        self.add_widget(self.password2)
        self.add_widget(self.cambio)


        # Set relative positions and sizes for elements using properties
        self.username_label.pos_hint = {'center_x': 0.5, 'y': 0.6}
        self.username_label.size_hint_y = 0.1

        self.password_label.pos_hint = {'center_x': 0.5, 'y': 0.45}
        self.password_label.size_hint_y = 0.1
       
        self.password1.pos_hint = {'center_x': 0.5, 'top': self.username_label.pos_hint.get("y") + 0.03, 'width': 0.7}
        self.password1.size_hint_y = 0.07
        self.password1.size_hint_x = 0.3


        self.password2.pos_hint = {'center_x': 0.5, 'top': self.password_label.pos_hint.get("y") + 0.03, 'width': 0.7}
        self.password2.size_hint_y = 0.07
        self.password2.size_hint_x = 0.3

        self.cambio.pos_hint = {'center_x': 0.5, 'top': 0.2}
        self.cambio.size_hint_y = 0.1
        self.cambio.size_hint_x = 0.3

        #BOTON PARA VOLVER
        self.atras = Button(text="VOLVER", on_press=self.switch_to_login, font_size=25,font_name=font)
        self.add_widget(self.atras)

        self.atras.pos_hint = {'center_x': 0.89, 'top': 0.95}
        self.atras.size_hint_y = 0.1
        self.atras.size_hint_x = 0.156

        # DESIGN
        self.cambio.background_color=(0.5,0.5,0.5)

        self.cambio.color=(1,1,1)

    def switch_to_login(self, instance):
        self.manager.current = 'appAdmin'

    def on_cambio_press(self, instance):
        # Implement login logic here
        # (e.g., validate username and password against a database)
        password1 = self.password1.text
        password2 = self.password2.text
        cedula = self.manager.get_screen('login').username.text
        current_screen = App.get_running_app().root.current_screen
        cedula=current_screen.username
        bn = admin()
        
        self.popup = Popup(title='Info', content=Label(text=bn.updatePassword([password2, password1, cedula])),
        auto_dismiss=True, size_hint=(None, None), size=(700, 200))
        self.popup.open()
        self.password1.text=''
        self.password2.text=''

