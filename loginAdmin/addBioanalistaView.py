# paquetes
from administracion.admin import admin

from administracion.admin import admin
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import random
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class appAddBioanalista(Screen):
    def __init__(self, **kwargs):
        super(appAddBioanalista, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        font="./fuentes/coolvetica.otf"

        #LABEL E INPUT NOMBRE

        self.nombre = TextInput(hint_text="Nombre del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.apellido = TextInput(hint_text="Apellido del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.cedula = TextInput(hint_text="Cedula del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.especialidad = TextInput(hint_text="Especialidad del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.telefono = TextInput(hint_text="telefono del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.email = TextInput(hint_text="Email del Bioanalista", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
       
        
        self.add_widget(self.nombre)

        self.nombre.pos_hint = {'center_x': 0.2, 'top': 0.90, 'width': 0.7}
        self.nombre.size_hint_y = 0.07
        self.nombre.size_hint_x = 0.3

        self.add_widget(self.apellido)

        self.apellido.pos_hint = {'center_x': 0.2, 'top': 0.80, 'width': 0.7}
        self.apellido.size_hint_y = 0.07
        self.apellido.size_hint_x = 0.3 

        self.add_widget(self.cedula)

        self.cedula.pos_hint = {'center_x': 0.2, 'top': 0.70, 'width': 0.7}
        self.cedula.size_hint_y = 0.07
        self.cedula.size_hint_x = 0.3 

        self.add_widget(self.especialidad)

        self.especialidad.pos_hint = {'center_x': 0.2, 'top': 0.60, 'width': 0.7}
        self.especialidad.size_hint_y = 0.07
        self.especialidad.size_hint_x = 0.3 

        self.add_widget(self.telefono)

        self.telefono.pos_hint = {'center_x': 0.2, 'top': 0.50, 'width': 0.7}
        self.telefono.size_hint_y = 0.07
        self.telefono.size_hint_x = 0.3     
 
        
        self.add_widget(self.email)

        self.email.pos_hint = {'center_x': 0.2, 'top': 0.40, 'width': 0.7}
        self.email.size_hint_y = 0.07
        self.email.size_hint_x = 0.3  

        #BOTON PARA AGREGAR BIOANALISTA
        self.addBioanalista = Button(text="AGREGAR BIOANALISTA", on_press=self.btnBioanalista, font_size=25,font_name=font)
        self.add_widget(self.addBioanalista)

        self.addBioanalista.pos_hint = {'center_x': 0.60, 'top': 0.16}
        self.addBioanalista.size_hint_y = 0.1
        self.addBioanalista.size_hint_x = 0.3

        #BOTON PARA VOLVER
        self.atras = Button(text="VOLVER", on_press=self.switch_to_admin, font_size=25,font_name=font)
        self.add_widget(self.atras)

        self.atras.pos_hint = {'center_x': 0.89, 'top': 0.95}
        self.atras.size_hint_y = 0.1
        self.atras.size_hint_x = 0.156

    def switch_to_admin(self, instance):
        self.manager.current = 'appAdmin'

    # Agregar Bioanalista a la DB
    def btnBioanalista(self, instance):
        name = self.nombre.text
        lname = self.apellido.text
        id = self.cedula.text
        especialidad = self.especialidad.text
        contact = self.telefono.text
        mail = self.email.text
        password=random.randint(7000000,9000000)

        bn = admin()

        self.popup = Popup(title='Info', content=Label(text=bn.addBioanalista([name, lname, especialidad, contact, mail, password, id])),
        auto_dismiss=True, size_hint=(None, None), size=(500, 200))
        
        self.popup2 = Popup(title='Info', content=Label(text="Bioanalista Password: " + str(password)),
        auto_dismiss=True, size_hint=(None, None), size=(500, 200))        
        
        self.nombre.text=''
        self.apellido.text=''
        self.cedula.text=''
        self.especialidad.text=''
        self.telefono.text=''
        self.email.text=''

        self.popup.open()

        self.popup2.open()

