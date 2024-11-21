from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sys
import os

# Add the parent directory of 'administracion' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from administracion.admin import admin

class appBusquedaBioanalistaView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        font = "./fuentes/coolvetica.otf"  

        # Go Back Button
        self.go_back_button = Button(text="Volver", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5}, on_press=self.go_back)
        self.layout.add_widget(self.go_back_button)

        # Reload Button
        self.reload = Button(text="actualizar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.8}, on_press=self.busqueda)
        self.layout.add_widget(self.reload)

        # Create ScrollView initially empty
        self.scrollview = ScrollView(size_hint=(None, None), size=(1000, 1000),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.34}, do_scroll_y=True)
        self.scrollview.add_widget(self.layout)

        self.add_widget(self.scrollview)

        # Perform initial search when the screen enters
        self.busqueda(None)

    def clear_widgets(self):
        for widget in self.layout.children[:]:
            if widget not in (self.go_back_button, self.reload):
                self.layout.remove_widget(widget)

    def busqueda(self, instance):
        self.clear_widgets()

        bn = admin()
        bioanalistas = bn.busquedaBioanalistas2()
        self.bioanalists = []

        for bioanalista in bioanalistas:
            nombre, apellido, cedula, especialidad, telefono = bioanalista
            button_text = f'Bioanalista: {nombre} {apellido},c.i {cedula}, especialidad:{especialidad}, telefono:{telefono}'
            button = Button(text=button_text, size_hint=(1, None), height=80)
            self.layout.add_widget(button)
            self.bioanalists.append(button)

    def go_back(self, instance):
        self.manager.current = 'appAdmin'
