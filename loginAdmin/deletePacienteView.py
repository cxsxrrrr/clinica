from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
#packages
import sys
sys.path.append('../clinica')
from administracion.admin import admin
# (Assuming 'admin' is imported as explained previously)
# from administracion.admin import admin

class ScrollableButtonsApp(App):
    def build(self):
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        Window.clearcolor = (18/255, 18/255, 18/255)  # Darkmode background
        font = "./fuentes/coolvetica.otf"  # Assuming font path is correct

        # TextInput adjusted for visibility
        self.cedula = TextInput(hint_text="Cedula, nombre, apellido, sexo", multiline=False, font_name=font,
                                font_size=40, size_hint_y=None, height=80, padding=[5, 20, 0, 0])

        self.cedula.bind(on_text_validate=self.on_enter)
        self.layout.add_widget(self.cedula)

        # Create ScrollView initially empty
        self.scrollview = ScrollView(size_hint=(None, None), size=(1000, 1000),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.34}, do_scroll_y=True)
        self.scrollview.add_widget(self.layout)

        return self.scrollview

    def on_enter(self, instance):
        # Remove all widgets except the cedula input
        for widget in self.layout.children:
            if widget != self.cedula:
                self.layout.remove_widget(widget)

        bn=admin()
        pacientes=bn.busquedaPacientes(self.cedula.text)
        print(pacientes)
        patients=[]
        for paciente in pacientes:
            try:
                nombre, apellido, cedula = paciente
                button_text = f'Paciente: {nombre} {apellido}, {cedula}'
                
                patients.append(Button(text=button_text, size_hint=(1, None), height=80))
                print(patients)

                # Add functionality to the button (example)
                patients[0].bind(on_press=lambda instance: self.delete(cedula))  # Assuming you have a method
                self.layout.add_widget(patients[0])
            except Exception as e:
                print(f"Error creating button for patient: {e}")

        self.cedula.text = ''  # Clear the cedula input after processing
    def delete(self, cedula):
        self.popup = Popup(title='Info', content=Label(text=cedula),
        auto_dismiss=True, size_hint=(None, None), size=(500, 200))
        self.popup.open()

if __name__ == '__main__':
    ScrollableButtonsApp().run()