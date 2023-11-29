from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from main import GiveData

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 24
            bold: True
            text: 'Welcome to my Training App!'
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'START'
                font_size: 24
                on_press: root.start_button_pressed()
            Button:
                text: 'ACHIEVEMENTS'
                font_size: 24
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'STATISTICS'
                font_size: 24
            Button:
                text: 'QUIT'
                font_size: 24
<StartScreen>:
    kg_label: kg_label
    reps_label: reps_label
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: kg_label
            text: 'Weight data is being processed!'
        Label:
            id: reps_label
            text: 'Repetition data is being processed!'

""")


class MenuScreen(Screen):
    def start_button_pressed(self):
        self.manager.current = 'start'


class StartScreen(Screen):
    kg = NumericProperty(0)
    reps = NumericProperty(0)

    def on_enter(self):
        data_provider = GiveData()
        self.kg = data_provider.give()[0]
        self.reps = data_provider.give()[1]
        self.kg_label.text = f'Kilograms: {self.kg}kg'
        self.reps_label.text = f'Number of reps done: {self.reps}'


class MainMenuApp(App):
    def build(self):
        sm = ScreenManager()
        menu_screen = MenuScreen(name="menu")
        start_screen = StartScreen(name="start")
        sm.add_widget(menu_screen)
        sm.add_widget(start_screen)

        return sm


if __name__ == "__main__":
    MainMenuApp().run()
