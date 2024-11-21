#packages

import sys
import os

# Add the parent directory of 'administracion' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from appAdmin import appAdministrador
from addPacienteView import appAddPaciente
from addBioanalistaView import appAddBioanalista
from deletePacienteView import appDeletePacienteView
from deleteBioanalistaView import appDeleteBioanalistaView
from busquedaPacienteView import appBusquedaPacienteView
from busquedaBioanalistaView import appBusquedaBioanalistaView
from generarResultadosView import generarResultados
# kivy imports
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.screenmanager import NoTransition  
#sql imports
import sqlite3

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        # VENTANA
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        #FUENTE A USAR

        font="./fuentes/coolvetica.otf"

        wimg = Image(source='../img/mylogo.png', size_hint=(None, None), size=(200, 200), allow_stretch=True, pos_hint={'center_x': 0.5, 'y': 0.67})
        self.add_widget(wimg)

        # Create labels for username and password
        self.username_label = Label(text="Username:", font_name=font, font_size=25)
        self.password_label = Label(text="Password:", font_name=font, font_size=25)

        # Create text input fields for username and password
        self.username = TextInput(hint_text="Enter your username", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.role = Label(text="Administracion", font_name=font, font_size=25)
        self.password = TextInput(password=True, multiline=False, hint_text="Enter your password", font_name=font, font_size=20, padding=[5, 15, 0, 0])

        # Create a login button
        self.login_button = Button(text="Login", on_press=self.on_login_press, font_name=font, font_size=25)
    
        # Add widgets to the layout with relative positioning
        self.add_widget(self.username_label)
        self.add_widget(self.password_label)
        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.login_button)
        self.add_widget(self.role)

        # Set relative positions and sizes for elements using properties
        self.username_label.pos_hint = {'center_x': 0.5, 'y': 0.6}
        self.username_label.size_hint_y = 0.1

        self.password_label.pos_hint = {'center_x': 0.5, 'y': 0.45}
        self.password_label.size_hint_y = 0.1
       
        self.username.pos_hint = {'center_x': 0.5, 'top': self.username_label.pos_hint.get("y") + 0.03, 'width': 0.7}
        self.username.size_hint_y = 0.07
        self.username.size_hint_x = 0.3


        self.password.pos_hint = {'center_x': 0.5, 'top': self.password_label.pos_hint.get("y") + 0.03, 'width': 0.7}
        self.password.size_hint_y = 0.07
        self.password.size_hint_x = 0.3

        self.login_button.pos_hint = {'center_x': 0.5, 'top': self.password.pos_hint.get("top") -0.1}
        self.login_button.size_hint_y = 0.1
        self.login_button.size_hint_x = 0.3

        self.role.pos_hint = {'center_x': 0.097, 'y': 0.45}
        # DESIGN
        self.login_button.background_color=(0.5,0.5,0.5)

        self.login_button.color=(1,1,1)

        self.popup = Popup(title='Error', content=Label(text='Por favor, ingresa una cedula valida, sin caracteres especiales ni letras.'),
              auto_dismiss=True, size_hint=(None, None), size=(770, 300))
        self.popupPassword = Popup(title='Error', content=Label(text='Cédula o Contraseña incorrectas. Por favor, intenta de nuevo.'),
              auto_dismiss=True, size_hint=(None, None), size=(770, 300))
    def on_login_press(self, instance):
        username = self.username.text
        password = self.password.text
        username = username.strip()
           
            
        try:
            # Conexion a la db
            conn = sqlite3.connect('clinicamalestar.db')

            # crear cursor para ejecutar queries
            cursor = conn.cursor()
            def detectNonNumberCharacters(id):
                return any(not c.isdigit() for c in id)
            
            if (detectNonNumberCharacters(username)==False):
                statement = f"SELECT cedula from AdminLg WHERE cedula='{username}' AND password = '{password}';"

                cursor.execute(statement)
                if not cursor.fetchone():
                    self.popupPassword.open()
                else:
                    
                    self.manager.current = 'appAdmin' 
            else:
                self.popup.open()
            # Commit a los cambios
            conn.commit()
            self.username.text=''
            self.password.text=''
        except sqlite3.Error as e:
            # Handle any errors that occur during the database connection or query execution
            print(f"An error occurred: {e}")

class MyApp(App):

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(appAdministrador(name='appAdmin'))
        sm.add_widget(appAddPaciente(name='addPacienteView'))
        sm.add_widget(appAddBioanalista(name='addBioanalistaView')) 
        sm.add_widget(appDeletePacienteView(name='deletePacienteView'))          
        sm.add_widget(appDeleteBioanalistaView(name='deleteBioanalistaView'))   
        sm.add_widget(appBusquedaPacienteView(name='busquedaPacienteView'))   
        sm.add_widget(appBusquedaBioanalistaView(name='busquedaBioanalistaView'))     
        sm.add_widget(generarResultados(name='generarResultadosView'))
        #frsf
        return sm



if __name__ == '__main__':
    MyApp().run()