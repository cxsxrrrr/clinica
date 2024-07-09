from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import sys

# Adjust sys.path as needed
sys.path.append('../clinica')
from administracion.admin import admin

class appDeleteBioanalistaView(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        font = "./fuentes/coolvetica.otf"  # Assuming font path is correct

        # Go Back Button
        self.go_back_button = Button(text="Volver", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5}, on_press=self.go_back)
        
        self.layout.add_widget(self.go_back_button)
        self.eliminarBioanalista = Button(text="Eliminar Bioanalista", on_press=lambda x:self.switch_to_eliminarBioanalista(self), font_size=25, pos_hint={'center_x': 0.7} ,font_name=font)
        # TextInput adjusted for visibility
        self.cedula = TextInput(hint_text="Cedula, nombre, apellido, sexo", multiline=False, font_name=font,
                                font_size=40, size_hint_y=None, height=80, padding=[5, 20, 0, 0])

        self.cedula.bind(on_text_validate=self.busqueda)
        self.layout.add_widget(self.cedula)

        # Create ScrollView initially empty
        self.scrollview = ScrollView(size_hint=(None, None), size=(1000, 1000),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.34}, do_scroll_y=True)
        self.scrollview.add_widget(self.layout)

        self.add_widget(self.scrollview)

    def busqueda(self, instance):  # Corrected to accept 'instance'
        # ... (your existing logic to clear previous widgets)
            bn = admin()
            bioanalistas = bn.busquedaBioanalista(self.cedula.text)
            print(bioanalistas)
            self.bioanalists = []

            for bioanalista in bioanalistas:   
         
                    nombre, apellido, cedula = bioanalista
                    button_text = f'Bioanalista: {nombre} {apellido}, {cedula}'
                    button = Button(text=button_text, size_hint=(1, None), height=80)
                    button.bind(on_press=lambda instance, cedula=cedula: self.delete(instance, cedula))
                    self.layout.add_widget(button)
                    self.bioanalists.append(button)

            self.cedula.text = ''  

    def delete(self, instance, cedula):
        bn = admin()
        result = bn.deleteBioanalista(cedula)
        if result:
            self.layout.remove_widget(instance)  # Remove the button from the layout

            # Create a label with the result of the deletion
            content = Label(text=f'Bioanalista con cedula {cedula} eliminado')

            # Create the popup with the label as its content
            self.popup = Popup(title='Info', content=content,
                               auto_dismiss=True, size_hint=(None, None), size=(500, 200))
            self.popup.open()
        else:
            # Create a label with the error message
            content = Label(text=f'Error al eliminar el Bioanalista con cedula {cedula}')

            # Create the popup with the label as its content
            self.popup = Popup(title='Error', content=content,
                               auto_dismiss=True, size_hint=(None, None), size=(500, 200))
            self.popup.open() 

    def go_back(self, instance):
        self.manager.current = 'appAdmin'
