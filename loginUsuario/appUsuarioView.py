from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import sys
from kivy.uix.image import Image

# Asegúrate de que el path esté configurado correctamente para importar desde '../clinica'
sys.path.append('../clinica')
from administracion.admin import admin
# Importa LoginScreen desde el archivo adecuado (suponiendo que es loginUser.py)
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager



class UsuarioScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        font = "./fuentes/coolvetica.otf"  
        wimg = Image(source='../img/mylogo.png', size_hint=(None, None), size=(100, 100), allow_stretch=True, pos_hint={'center_x': 0.5, 'y': 0.8})
        self.add_widget(wimg)
        # Go Back Button
        self.go_back_button = Button(text="Logout", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5}, on_press=self.go_back, font_name=font)
        self.layout.add_widget(self.go_back_button)

        # Reload Button
        self.reload = Button(text="actualizar", size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.8}, on_press=self.busqueda, font_name=font)
        self.layout.add_widget(self.reload)

        # Create ScrollView initially empty
        self.scrollview = ScrollView(size_hint=(None, None), size=(1000, 1000),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.34}, do_scroll_y=True)
        self.scrollview.add_widget(self.layout)

        self.add_widget(self.scrollview)


        # No llames a busqueda aquí, espera hasta que se establezca la pantalla actual correctamente

    def clear_widgets(self):
        for widget in self.layout.children[:]:
            if widget not in (self.go_back_button, self.reload):
                self.layout.remove_widget(widget)

    def busqueda(self, instance):
        current_screen = App.get_running_app().root.current_screen
        if current_screen:
            username = current_screen.username
            # Aquí realizas la búsqueda de resultados usando el nombre de usuario
            bn = admin()
            resultados = bn.busquedaResultados(username)  # Pasar el nombre de usuario
            self.clear_widgets()
            self.patients = []

            for result in resultados:
                resultado, fecha_resultado, bioanalista = result
                button_text = f'Resultado: {resultado}\nFecha: {fecha_resultado}\nBioanalista: {bioanalista}'
                button = Button(text=button_text, size_hint=(1, None), height=80, font_name="./fuentes/coolvetica.otf")
                self.layout.add_widget(button)

    def go_back(self, instance):
        # Cambiar de vuelta a la pantalla de administración (appAdmin)
        self.manager.current = 'login'

