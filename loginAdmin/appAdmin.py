# kivy imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
import sys
import os

# Add the parent directory of 'administracion' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class appAdministrador(Screen):
    def __init__(self, **kwargs):
        
        
        super(appAdministrador, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background

        fuente="./fuentes/coolvetica.otf"
        wimg = Image(source='../img/mylogo.png', size_hint=(None, None), size=(500, 500), allow_stretch=True, pos_hint={'center_x': 0.67, 'y': 0.1})
        self.add_widget(wimg)
        self.button = Button(text="Cerrar sesion", on_press=self.switch_to_home, font_size=25,font_name=fuente)
        self.add_widget(self.button)

        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17



        #AGREGAR BIOANALISTA BOTON
        self.agregarBioanalista = Button(text="Agregar Bioanalista", on_press=self.switch_to_agregarBioanalista, font_size=25, font_name=fuente)
        self.add_widget(self.agregarBioanalista)

        self.agregarBioanalista.pos_hint = {'center_x': 0.13, 'top': 0.8}
        self.agregarBioanalista.size_hint_y = 0.1
        self.agregarBioanalista.size_hint_x = 0.30

        analisis = Image(source='../img/analisis.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.8})
        self.add_widget(analisis)
        
        #ELIMINAR BIOANALISTA BOTON

        self.eliminarBioanalista = Button(text="Eliminar Bioanalista", on_press=self.switch_to_eliminarBioanalista, font_size=25,font_name=fuente)
        self.add_widget(self.eliminarBioanalista)

        self.eliminarBioanalista.pos_hint = {'center_x': 0.13, 'top': 0.7}
        self.eliminarBioanalista.size_hint_y = 0.1
        self.eliminarBioanalista.size_hint_x = 0.30    
        enfermeria = Image(source='../img/enfermeria.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.7})
        self.add_widget(enfermeria)
        #AGREGAR PACIENTE
        self.agregarPaciente = Button(text="Agregar Paciente", on_press=self.switch_to_agregarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.agregarPaciente)

        self.agregarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.6}
        self.agregarPaciente.size_hint_y = 0.1
        self.agregarPaciente.size_hint_x = 0.30    
        
        carpeta = Image(source='../img/carpeta.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.6})
        self.add_widget(carpeta)
        #ELIMINAR PACIENTE    
        self.eliminarPaciente = Button(text="Eliminar Paciente", on_press=self.switch_to_eliminarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.eliminarPaciente)

        self.eliminarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.50}
        self.eliminarPaciente.size_hint_y = 0.1
        self.eliminarPaciente.size_hint_x = 0.30 

        clinica = Image(source='../img/clinica.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.5})
        self.add_widget(clinica)

        #BUSQUEDA TODOS LOS PACIENTES  
        self.buscarPaciente = Button(text="PACIENTES", on_press=self.switch_to_buscarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.buscarPaciente)
        self.buscarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.40}
        self.buscarPaciente.size_hint_y = 0.1
        self.buscarPaciente.size_hint_x = 0.30 

        medicamento = Image(source='../img/medicamento.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.4})
        self.add_widget(medicamento)

        #BUSQUEDA TODOS LOS BIOANALISTAS 
        self.buscarBioanalista = Button(text="BIOANALISTAS", on_press=self.switch_to_buscarBioanalista, font_size=25,font_name=fuente)
        self.add_widget(self.buscarBioanalista)
        self.buscarBioanalista.pos_hint = {'center_x': 0.13, 'top': 0.30}
        self.buscarBioanalista.size_hint_y = 0.1
        self.buscarBioanalista.size_hint_x = 0.30 

        construccion = Image(source='../img/construccion.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.3})
        self.add_widget(construccion)

        self.generarResultados = Button(text="Generar resultados", on_press=self.switch_to_generarResultados, font_size=25,font_name=fuente)
        self.add_widget(self.generarResultados)
        self.generarResultados.pos_hint = {'center_x': 0.13, 'top': 0.20}
        self.generarResultados.size_hint_y = 0.1
        self.generarResultados.size_hint_x = 0.30 

        resultados = Image(source='../img/resultados.png', size_hint=(None, None), size=(50, 50), allow_stretch=True, pos_hint={'center_x': 0.323, 'top': 0.2})
        self.add_widget(resultados)

    #VOLVER
    def switch_to_home(self, instance):
        self.manager.current = 'login'
    #BIOANALISTAS
    def switch_to_agregarBioanalista(self, instance):
        self.manager.current = 'addBioanalistaView'

    def switch_to_eliminarBioanalista(self, instance):
        self.manager.current = 'deleteBioanalistaView'
    #PACIENTES
    def switch_to_agregarPaciente(self, instance):
        self.manager.current = 'addPacienteView'

    def switch_to_eliminarPaciente(self, instance):
        self.manager.current = 'deletePacienteView'

    def switch_to_buscarPaciente(self, instance):
        self.manager.current = 'busquedaPacienteView'

    def switch_to_buscarBioanalista(self, instance):
        self.manager.current = 'busquedaBioanalistaView'

    def switch_to_generarResultados(self, instance):
        self.manager.current = 'generarResultadosView'