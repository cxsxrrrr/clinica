# paquetes
from administracion.admin import admin

from administracion.admin import admin
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

class appAddPaciente(Screen):
    def __init__(self, **kwargs):
        super(appAddPaciente, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        font="./fuentes/coolvetica.otf"

        #LABEL E INPUT NOMBRE

        self.nombre = TextInput(hint_text="Nombre del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.apellido = TextInput(hint_text="Apellido del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.cedula = TextInput(hint_text="Cedula del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.fecha_nacimiento = TextInput(hint_text="Fecha de nacimiento del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.sexo = TextInput(hint_text="Sexo del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.telefono = TextInput(hint_text="Telefono del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.direccion = TextInput(hint_text="Direccion del paciente", multiline=True, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.email = TextInput(hint_text="Correo del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])

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

        self.add_widget(self.fecha_nacimiento)

        self.fecha_nacimiento.pos_hint = {'center_x': 0.2, 'top': 0.60, 'width': 0.7}
        self.fecha_nacimiento.size_hint_y = 0.07
        self.fecha_nacimiento.size_hint_x = 0.3 

        self.add_widget(self.sexo)

        self.sexo.pos_hint = {'center_x': 0.2, 'top': 0.50, 'width': 0.7}
        self.sexo.size_hint_y = 0.07
        self.sexo.size_hint_x = 0.3         


        self.add_widget(self.telefono)

        self.telefono.pos_hint = {'center_x': 0.2, 'top': 0.40, 'width': 0.7}
        self.telefono.size_hint_y = 0.07
        self.telefono.size_hint_x = 0.3     

        self.add_widget(self.direccion)

        self.direccion.pos_hint = {'center_x': 0.2, 'top': 0.30, 'width': 0.7}
        self.direccion.size_hint_y = 0.07
        self.direccion.size_hint_x = 0.3  
        
        self.add_widget(self.email)

        self.email.pos_hint = {'center_x': 0.2, 'top': 0.20, 'width': 0.7}
        self.email.size_hint_y = 0.07
        self.email.size_hint_x = 0.3  

        #BOTON PARA AGREGAR PACIENTE
        self.addPaciente = Button(text="AGREGAR PACIENTE", on_press=self.btnPaciente, font_size=25,font_name=font)
        self.add_widget(self.addPaciente)

        self.addPaciente.pos_hint = {'center_x': 0.65, 'top': 0.16}
        self.addPaciente.size_hint_y = 0.1
        self.addPaciente.size_hint_x = 0.3

        #BOTON PARA VOLVER
        self.back = Button(text="VOLVER", on_press=self.switch_to_admin, font_size=25,font_name=font)
        self.add_widget(self.back)

        self.back.pos_hint = {'center_x': 0.89, 'top': 0.95}
        self.back.size_hint_y = 0.1
        self.back.size_hint_x = 0.156

    def switch_to_admin(self, instance):
        self.manager.current = 'appAdmin'

    # Agregar Paciente a la DB
    def btnPaciente(self, instance):
        name = self.nombre.text
        lname = self.apellido.text
        id = self.cedula.text
        date = self.fecha_nacimiento.text
        gender = self.sexo.text
        contact = self.telefono.text
        location = self.direccion.text
        mail = self.email.text
        bn = admin()

        self.popup = Popup(title='Info', content=Label(text=bn.addPaciente([name, lname, id, date, gender.upper(), contact, location, mail])),
        auto_dismiss=True, size_hint=(None, None), size=(500, 200))
        
        
        
        self.nombre.text=''
        self.apellido.text=''
        self.cedula.text=''
        self.apellido.text=''
        self.fecha_nacimiento.text=''
        self.sexo.text=''
        self.telefono.text=''
        self.direccion.text=''
        self.email.text=''

        self.popup.open()

