from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.label = Button(text="Welcome to the Home Screen")
        self.layout.add_widget(self.label)

        self.button = Button(text="Go to Settings")
        self.button.bind(on_press=self.switch_to_settings)
        self.layout.add_widget(self.button)

    def switch_to_settings(self, instance):
        self.manager.current = 'settings'

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.label = Button(text="Settings Screen")
        self.layout.add_widget(self.label)

        self.button = Button(text="Go to Home")
        self.button.bind(on_press=self.switch_to_home)
        self.layout.add_widget(self.button)

    def switch_to_home(self, instance):
        self.manager.current = 'home'

class MyScreenManager(ScreenManager):
    pass

class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()

        # Add screens to the ScreenManager
        screen_manager.add_widget(HomeScreen(name='home'))
        screen_manager.add_widget(SettingsScreen(name='settings'))

        return screen_manager

if __name__ == '__main__':
    TestApp().run()
