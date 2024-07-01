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


class RegisterScreen(Screen):

    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        # VENTANA
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        #FUENTE A USAR

        font="./fuentes/coolvetica.otf"

        self.button = Button(text="Volver", on_press=self.switch_to_login, font_size=25,font_name=font)
        self.add_widget(self.button)

        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17

        # Create labels for username and password
        self.username_label = Label(text="Ingresa tu cedula", font_name=font, font_size=25)
        self.password_label = Label(text="Crea tu contraseña", font_name=font, font_size=25)
        self.register = Label(text="Ya tienes una cuenta? Logeate Aqui!", font_name=font, font_size=25, on_press=self.switch_to_login)


        # Create text input fields for username and password
        self.username = TextInput(hint_text="Enter your username", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])

        self.password = TextInput(password=True, multiline=False, hint_text="Enter your password", font_name=font, font_size=20, padding=[5, 15, 0, 0])

        # Create a login button
        self.login_button = Button(text="Register", on_press=self.on_register_press, font_name=font, font_size=25)
    
        # Add widgets to the layout with relative positioning
        self.add_widget(self.username_label)
        self.add_widget(self.password_label)
        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.login_button)


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

        # DESIGN
        self.login_button.background_color=(0.5,0.5,0.5)

        self.login_button.color=(1,1,1)

        self.popup = Popup(title='Error', content=Label(text='Por favor, ingresa una cedula valida, sin caracteres especiales ni letras.'),
              auto_dismiss=True, size_hint=(None, None), size=(770, 300))
        self.popupPassword = Popup(title='Error', content=Label(text='Usted no se encuentra registrado en nuestra clinica.'),
              auto_dismiss=True, size_hint=(None, None), size=(770, 300))
 
    
    def switch_to_login(self, instance):
        self.manager.current = 'login'
    def on_register_press(self, instance):
        # Implement login logic here
        # (e.g., validate username and password against a database)
        username = self.username.text
        password = self.password.text
        username = username.strip()
        data=[username, password]
           
   
        try:
            # Conexion a la db
            conn = sqlite3.connect('clinicamalestar.db')

            # crear cursor para ejecutar queries
            cursor = conn.cursor()
            def detectNonNumberCharacters(id):
                return any(not c.isdigit() for c in id)
            
            if (detectNonNumberCharacters(username)==False):
                statement = f"SELECT cedula from Pacientes WHERE cedula='{username}';"

                cursor.execute(statement)
                if not cursor.fetchone():
                    #no se encuentra registrado
                    self.popupPassword.open()
                else:
                    insertClient_st = '''INSERT INTO PacienteLg(cedula, password) VALUES (?, ?)'''
                    cursor.execute(insertClient_st, data[:2])

                    self.popup2 = Popup(title='Info', content=Label(text="Usuario registrado exitosamente"),
                    auto_dismiss=True, size_hint=(None, None), size=(500, 200))
   
                    self.popup2.open()
                    cursor.close()
                    
            else:
                #cedula invalida
                self.popup.open()
            # Commit a los cambios
            conn.commit()
        except sqlite3.IntegrityError as e:
            # Manejar errores de integridad (por ejemplo, cédula duplicada)
            if "UNIQUE constraint failed" in str(e):
                self.popupError1 = Popup(title='Info', content=Label(text="Error: La cédula ya está registrada."),
                auto_dismiss=True, size_hint=(None, None), size=(500, 200))
                self.popupError1.open()

            else:
                self.popupError2 = Popup(title='Info', content=Label(text=f"Error de integridad en la base de datos: {e}"),
                auto_dismiss=True, size_hint=(None, None), size=(500, 200))
                self.popupError2.open()
                

        except sqlite3.Error as e:
        # Manejar otros errores generales de SQLite
            self.popupError3 = Popup(title='Info', content=Label(text=f"Error en la base de datos: {e}"),
            auto_dismiss=True, size_hint=(None, None), size=(500, 200))
            self.popupError3.open()
        

        finally:
        # Cerrar el cursor en todos los casos (éxito o error)
            if cursor:
                cursor.close()          
            cursor.close()
            conn.close()
            self.username.text=''
            self.password.text=''
