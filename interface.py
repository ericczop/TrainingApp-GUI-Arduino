from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
from main import GiveData
from kivy.core.window import Window
import threading

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: app.font_size
            bold: True
            color: app.dark_brown
            text: 'Welcome to my Training App!'

        BoxLayout:
            orientation: 'horizontal'
            padding: 5
            spacing: 10
            Button:
                text: 'START'
                font_size: app.font_size
                background_color: app.dark_brown
                on_press: root.start_button_pressed()
            Button:
                text: 'LAST TRAININGS'
                font_size: app.font_size
                background_color: app.dark_brown
        BoxLayout:
            orientation: 'horizontal'
            padding: 5
            spacing: 10
            Button:
                text: 'STATISTICS'
                font_size: app.font_size
                background_color: app.dark_brown          
            Button:
                text: 'QUIT'
                font_size: app.font_size
                background_color: app.dark_brown
                on_press: root.quit_app()

<CountdownScreen>:
    countdown_label: countdown_label
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: countdown_label
            font_size: 40
            color: app.dark_brown
            bold: True
            text: f'Start exercising in: {root.countdown}'

<StartScreen>:
    kg_label: kg_label
    reps_label: reps_label
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Your results:'
            bold: True
            font_size: 40
            canvas.before:
                Color:
                    rgba: app.light_brown
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            id: kg_label
            text: 'Weight data is being processed!'
            font_size: 20
            canvas.before:
                Color:
                    rgba: app.medium_brown
                Rectangle:
                    size: self.size
                    pos: self.pos
        Label:
            id: reps_label
            text: 'Repetition data is being processed!'
            font_size: 20
            canvas.before:
                Color:
                    rgba: app.dark_brown
                Rectangle:
                    size: self.size
                    pos: self.pos
        BoxLayout:
            orientation: 'horizontal'
            padding: 5
            spacing: 5
            Button:
                id: back_button
                text: 'Back'
                font_size: app.font_size
                size_hint: 0.5, 1 
                background_color: app.dark_brown
                on_press: root.go_back_to_menu()
                disabled: True
            Button:
                id: next_button
                text: 'Next Set'
                font_size: app.font_size
                background_color: app.dark_brown
                size_hint: 0.5, 1
                on_press: root.go_to_next_set()
                disabled: True
""")


class MenuScreen(Screen):
    def start_button_pressed(self):
        self.manager.current = 'countdown'
        # Start data processing in a separate thread
        data_thread = threading.Thread(target=self.process_data)
        data_thread.start()

    def process_data(self):
        data_provider = GiveData()
        kg, reps = data_provider.give()
        start_screen = self.manager.get_screen('start')
        start_screen.initialize_data(kg, reps)

    def quit_app(self):
        App.get_running_app().stop()


class CountdownScreen(Screen):
    countdown = NumericProperty(5)

    def on_enter(self):
        Clock.schedule_interval(self.update_countdown, 1)

    def update_countdown(self, dt):
        self.countdown -= 1
        self.countdown_label.text = f'Start exercising in: {self.countdown}'
        if self.countdown == 0:
            Clock.unschedule(self.update_countdown)
            self.manager.current = 'start'


class StartScreen(Screen):
    kg = NumericProperty(0)
    reps = NumericProperty(0)

    def initialize_data(self, kg, reps):
        self.kg = kg
        self.reps = reps
        self.kg_label.text = f'Kilograms assumed: {self.kg}kg'
        self.reps_label.text = f'Number of reps done: {self.reps}'
        self.ids.back_button.disabled = False
        self.ids.next_button.disabled = False

    def go_back_to_menu(self):
        self.manager.current = 'menu'

    def go_to_next_set(self):
        self.manager.current = 'countdown'


class MainMenuApp(App):
    font_size = NumericProperty(24)
    background_color = (214 / 255, 214 / 255, 177 / 255, 0.7)
    light_brown = ListProperty((63 / 255, 63 / 255, 55 / 255, 0.6))
    medium_brown = ListProperty((73 / 255, 67 / 255, 49 / 255, 0.8))
    dark_brown = ListProperty((73 / 255, 67 / 255, 49 / 255, 1))

    def build(self):
        Window.clearcolor = self.background_color
        sm = ScreenManager()
        menu_screen = MenuScreen(name="menu")
        countdown_screen = CountdownScreen(name="countdown")
        start_screen = StartScreen(name="start")
        sm.add_widget(menu_screen)
        sm.add_widget(countdown_screen)
        sm.add_widget(start_screen)
        return sm


if __name__ == "__main__":
    MainMenuApp().run()
