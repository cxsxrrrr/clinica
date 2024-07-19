# kivy imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image

class appAdministrador(Screen):
    def __init__(self, **kwargs):
        
        
        super(appAdministrador, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        wimg = Image(source='../img/mylogo.png', size_hint=(None, None), size=(500, 500), allow_stretch=True, pos_hint={'center_x': 0.67, 'y': 0.1})
        self.add_widget(wimg)
        fuente="./fuentes/coolvetica.otf"

        self.button = Button(text="Cerrar sesion", on_press=self.switch_to_home, font_size=25,font_name=fuente)
        self.add_widget(self.button)

        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17

        #ACTUALIZAR PASSWORD
        self.actualizarPassword = Button(text="Actualizar Contraseña", on_press=self.switch_to_update, font_size=25,font_name=fuente)

        self.actualizarPassword.pos_hint = {'center_x': 0.13, 'top': 0.7}
        self.actualizarPassword.size_hint_y = 0.1
        self.actualizarPassword.size_hint_x = 0.30    
        self.add_widget(self.actualizarPassword)

        #AGREGAR PACIENTE
        self.agregarPaciente = Button(text="Agregar Paciente", on_press=self.switch_to_agregarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.agregarPaciente)

        self.agregarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.6}
        self.agregarPaciente.size_hint_y = 0.1
        self.agregarPaciente.size_hint_x = 0.30    

        #ELIMINAR PACIENTE    
        self.eliminarPaciente = Button(text="Eliminar Paciente", on_press=self.switch_to_eliminarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.eliminarPaciente)

        self.eliminarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.50}
        self.eliminarPaciente.size_hint_y = 0.1
        self.eliminarPaciente.size_hint_x = 0.30 

        #BUSQUEDA TODOS LOS PACIENTES  
        self.buscarPaciente = Button(text="PACIENTES", on_press=self.switch_to_buscarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.buscarPaciente)
        self.buscarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.40}
        self.buscarPaciente.size_hint_y = 0.1
        self.buscarPaciente.size_hint_x = 0.30 

        self.generarResultados = Button(text="Generar resultados", on_press=self.switch_to_generarResultados, font_size=25,font_name=fuente)
        self.add_widget(self.generarResultados)
        self.generarResultados.pos_hint = {'center_x': 0.13, 'top': 0.30}
        self.generarResultados.size_hint_y = 0.1
        self.generarResultados.size_hint_x = 0.30 

    #VOLVER
    def switch_to_home(self, instance):
        self.manager.current = 'login'

    #ACTUALIZAR PASSWORD
    def switch_to_update(self, instance):
        self.manager.current = 'updatePassword'
    #PACIENTES
    def switch_to_agregarPaciente(self, instance):
        self.manager.current = 'addPacienteView'

    def switch_to_eliminarPaciente(self, instance):
        self.manager.current = 'deletePacienteView'

    def switch_to_buscarPaciente(self, instance):
        self.manager.current = 'busquedaPacienteView'

    def switch_to_generarResultados(self, instance):
        self.manager.current = 'generarResultadosView'