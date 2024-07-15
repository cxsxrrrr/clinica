import sys 
sys.path.append('../clinica')
from administracion.admin import admin

import sqlite3 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class generarResultados(Screen):
    def __init__(self, **kwargs):
        super(generarResultados, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background

        font="./fuentes/coolvetica.otf"

        self.button = Button(text="Volver", on_press=self.switch_to_home, font_size=25, font_name=font)
        self.add_widget(self.button)
        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17

        self.cedula = TextInput(hint_text="Ingresa cedula del paciente", multiline=False, font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.cedula.pos_hint = {'center_x': 0.2, 'top': 0.82, 'width': 0.7}
        self.cedula.size_hint_y = 0.07
        self.cedula.size_hint_x = 0.3
        self.add_widget(self.cedula)

        self.cedulaBioanalista = TextInput(multiline=False, hint_text="Cedula Bioanalista", font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.cedulaBioanalista.pos_hint = {'center_x': 0.2, 'top': 0.70, 'width': 0.7}
        self.cedulaBioanalista.size_hint_y = 0.07
        self.cedulaBioanalista.size_hint_x = 0.3
        self.add_widget(self.cedulaBioanalista)

        self.Resultado = TextInput(multiline=True, hint_text="Resultado", font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.Resultado.pos_hint = {'center_x': 0.2, 'top': 0.58, 'width': 0.7}
        self.Resultado.size_hint_y = 0.12
        self.Resultado.size_hint_x = 0.3
        self.add_widget(self.Resultado)

        self.fechaResultado = TextInput(multiline=False, hint_text="Fecha resultado", font_name=font, font_size=20, padding=[5, 15, 0, 0])
        self.fechaResultado.pos_hint = {'center_x': 0.2, 'top': 0.40, 'width': 0.7}
        self.fechaResultado.size_hint_y = 0.07
        self.fechaResultado.size_hint_x = 0.3
        self.add_widget(self.fechaResultado)

        self.addResultado = Button(text="AGREGAR RESULTADO", on_press=self.generarResultado, font_size=25, font_name=font)
        self.addResultado.pos_hint = {'center_x': 0.5, 'top': 0.16}
        self.addResultado.size_hint_y = 0.1
        self.addResultado.size_hint_x = 0.3
        self.add_widget(self.addResultado)

        self.popup = Popup(title='Error', content=Label(text='Por favor, ingresa una cedula valida, sin caracteres especiales ni letras.'),
                           auto_dismiss=True, size_hint=(None, None), size=(770, 300))
        self.popupPassword = Popup(title='Error', content=Label(text='No se encuentra registrado en nuestra clinica.'),
                                   auto_dismiss=True, size_hint=(None, None), size=(770, 300))

    # VOLVER
    def switch_to_home(self, instance):
        self.manager.current = 'appAdmin'

    def generarResultado(self, instance):
     

        idPaciente = self.cedula.text
        idBioanalista = self.cedulaBioanalista.text
        resultado = self.Resultado.text
        fechaResultado = self.fechaResultado.text


        try:
            # Conexion a la db
            conn = sqlite3.connect('clinicamalestar.db')

            # Crear cursor para ejecutar queries
            cursor = conn.cursor()

            def detectNonNumberCharacters(id):
                return any(not c.isdigit() for c in id)

            if not detectNonNumberCharacters(idPaciente) and not detectNonNumberCharacters(idBioanalista):
                statement = f"SELECT cedula FROM Pacientes WHERE cedula='{idPaciente}';"
                statement2 = f"SELECT cedula FROM Bioanalistas WHERE cedula='{idBioanalista}';"

                cursor.execute(statement)
                paciente = cursor.fetchone()
                cursor.execute(statement2)
                bioanalista = cursor.fetchone()

                if not paciente or not bioanalista:
                    # No se encuentra registrado
                    self.popupPassword.open()
                else:
                    insertClient_st = '''INSERT INTO Resultados(id_paciente, id_bioanalista, fecha_resultado, resultado) VALUES (?, ?, ?, ?)'''
                    cursor.execute(insertClient_st, (idPaciente, idBioanalista, fechaResultado, resultado))

                    self.popup2 = Popup(title='Info', content=Label(text="Resultado registrado exitosamente"),
                                        auto_dismiss=True, size_hint=(None, None), size=(500, 200))
                    self.popup2.open()
            else:
                # Cedula invalida
                self.popup.open()

            # Commit a los cambios solo si se insertaron datos
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
            # Cerrar el cursor y la conexión en todos los casos (éxito o error)
            if cursor:
                cursor.close()
            if conn:
                conn.close()

            # Limpiar campos
            self.cedula.text = ''
            self.cedulaBioanalista.text = ''
            self.Resultado.text = ''
            self.fechaResultado.text = ''
