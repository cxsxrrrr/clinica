# kivy imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class appAdministrador(Screen):
    def __init__(self, **kwargs):
        
        
        super(appAdministrador, self).__init__(**kwargs)
        self.layout = RelativeLayout()
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background

        fuente="./fuentes/coolvetica.otf"

        self.button = Button(text="Cerrar sesion", on_press=self.switch_to_home, font_size=25,font_name=fuente)
        self.add_widget(self.button)

        self.button.pos_hint = {'center_x': 0.1, 'top': 0.98}
        self.button.size_hint_y = 0.09
        self.button.size_hint_x = 0.17
 

        #AGREGAR PACIENTE
        self.agregarPaciente = Button(text="Agregar Paciente", on_press=self.switch_to_agregarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.agregarPaciente)

        self.agregarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.73}
        self.agregarPaciente.size_hint_y = 0.1
        self.agregarPaciente.size_hint_x = 0.30    

        #ELIMINAR PACIENTE    
        self.eliminarPaciente = Button(text="Eliminar Paciente", on_press=self.switch_to_eliminarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.eliminarPaciente)

        self.eliminarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.6}
        self.eliminarPaciente.size_hint_y = 0.1
        self.eliminarPaciente.size_hint_x = 0.30 

        #BUSQUEDA TODOS LOS PACIENTES  
        self.buscarPaciente = Button(text="PACIENTES", on_press=self.switch_to_buscarPaciente, font_size=25,font_name=fuente)
        self.add_widget(self.buscarPaciente)
        self.buscarPaciente.pos_hint = {'center_x': 0.13, 'top': 0.49}
        self.buscarPaciente.size_hint_y = 0.1
        self.buscarPaciente.size_hint_x = 0.30 



    #VOLVER
    def switch_to_home(self, instance):
        self.manager.current = 'login'

    #PACIENTES
    def switch_to_agregarPaciente(self, instance):
        self.manager.current = 'addPacienteView'

    def switch_to_eliminarPaciente(self, instance):
        self.manager.current = 'deletePacienteView'

    def switch_to_buscarPaciente(self, instance):
        self.manager.current = 'addPacienteView'

    def switch_to_buscarBioanalista(self, instance):
        self.manager.current = 'deletePacienteView'