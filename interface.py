from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.properties import NumericProperty, ListProperty
from kivy.clock import Clock
from kivymd.uix.list import OneLineListItem
from main import GiveData
import threading
import pandas as pd

Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
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
                on_press: root.last_trainings_button_pressed()
        BoxLayout:
            orientation: 'horizontal'
            padding: 5
            spacing: 10
            Button:
                text: 'STATISTICS'
                font_size: app.font_size
                background_color: app.dark_brown          
                on_press: root.statistics_button_pressed()
            Button:
                text: 'QUIT'
                font_size: app.font_size
                background_color: app.dark_brown
                on_press: root.quit_app()

<CountdownScreen>:
    canvas.before:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
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
    canvas.before:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
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
        Label:
            text: 'Enter exercise name below:'
            font_size: 20
            canvas.before:
                Color:
                    rgba: app.brown
                Rectangle:
                    size: self.size
                    pos: self.pos
        TextInput:
            id: exercise_name_input
            hint_text: 'Exercise Name'
            font_size: app.font_size
            background_color: app.brown2
            halign: 'center'
            padding_y: [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            disabled: True
        BoxLayout:
            orientation: 'horizontal'
            padding: 5
            spacing: 5
            Button:
                id: save_button
                text: 'Save'
                font_size: app.font_size
                background_color: app.dark_green
                size_hint: 0.5, 1
                disabled: True
                on_press: root.save_button_pressed()
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
<LastTrainingScreen>:
    canvas.before:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 50
            size_hint: 1, 0.5
            bold: True
            color: app.dark_brown
            text: 'Last Training Data'

        ScrollView:
            MDList:
                id: container
                color: app.dark_brown

        Button:
            text: 'Back to Menu'
            font_size: app.font_size
            background_color: app.dark_brown
            size_hint: 1, 0.5
            on_press: root.go_back_to_menu()

<StatisticsScreen>:
    canvas.before:
        Color:
            rgba: app.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 50
            size_hint: 1, 0.1
            bold: True
            color: app.dark_brown
            text: 'Exercise Statistics'

        ScrollView:
            MDList:
                id: statistics_container
                color: app.dark_brown

        Button:
            text: 'Back to Menu'
            font_size: app.font_size
            background_color: app.dark_brown
            size_hint: 1, 0.1
            on_press: root.go_back_to_menu()


""")


class MenuScreen(Screen):
    def start_button_pressed(self):
        self.manager.current = 'countdown'
        # Start data processing in a separate thread
        data_thread = threading.Thread(target=self.process_data)
        data_thread.start()

    def last_trainings_button_pressed(self):
        self.manager.current = 'last_training'

    def statistics_button_pressed(self):
        self.manager.current = 'statistics'

    def process_data(self):
        data_provider = GiveData()
        kg, reps = data_provider.give()
        start_screen = self.manager.get_screen('start')
        start_screen.initialize_data(kg, reps)

    def quit_app(self):
        MDApp.get_running_app().stop()


class CountdownScreen(Screen):
    countdown = NumericProperty(5)

    def on_pre_enter(self):
        self.countdown = 5

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
        # self.save_data_to_csv(kg, reps, filename='training_data.csv')
        self.kg_label.text = f'Kilograms: {self.kg}kg'
        self.reps_label.text = f'Number of reps done: {self.reps}'
        self.ids.exercise_name_input.disabled = False
        self.ids.save_button.disabled = False

    def process_data(self):
        data_provider = GiveData()
        kg, reps = data_provider.give()
        start_screen = self.manager.get_screen('start')
        start_screen.initialize_data(kg, reps)

    def go_back_to_menu(self):
        self.reset()
        self.manager.current = 'menu'

    def go_to_next_set(self):
        self.reset()
        self.manager.current = 'countdown'
        data_thread = threading.Thread(target=self.process_data)
        data_thread.start()

    def reset(self):
        self.ids.back_button.disabled = True
        self.ids.next_button.disabled = True
        self.kg_label.text = 'Weight data is being processed!'
        self.reps_label.text = 'Repetition data is being processed!'
        self.ids.exercise_name_input.text = ''  # Clear the exercise name input

    def save_data_to_csv(self, kg, reps, filename='training_data.csv'):
        exercise_name = self.ids.exercise_name_input.text  # Get the exercise name
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['ExerciseName', 'Kilograms', 'Repetitions'])

        new_data = pd.DataFrame({'ExerciseName': [exercise_name], 'Kilograms': [kg], 'Repetitions': [reps]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(filename, index=False)

    def save_button_pressed(self):
        self.save_data_to_csv(self.kg, self.reps, filename='training_data.csv')
        self.ids.back_button.disabled = False
        self.ids.next_button.disabled = False
        self.ids.exercise_name_input.disabled = True
        self.ids.save_button.disabled = True


class LastTrainingScreen(Screen):
    def on_pre_enter(self):
        training_data = self.load_training_data()
        try:
            for entry in training_data:
                item = OneLineListItem(text=entry)
                item.bg_color = (73 / 255, 67 / 255, 49 / 255, 0.8)  # Background color
                self.ids.container.add_widget(item)
        except TypeError:
            pass

    def go_back_to_menu(self):
        self.ids.container.clear_widgets()
        self.manager.current = 'menu'

    def load_training_data(self, filename='training_data.csv'):
        try:
            df = pd.read_csv(filename)
            if not df.empty:
                training_data = []
                for index, row in df.iterrows():
                    data_entry = f'Exercise: {row["ExerciseName"]} | Kilograms: {row["Kilograms"]} | Repetitions: {row["Repetitions"]}'
                    training_data.append(data_entry)
                return training_data
        except FileNotFoundError:
            self.ids.container.add_widget(OneLineListItem(text="No training data available."))


class StatisticsScreen(Screen):
    def on_pre_enter(self):
        statistics_data = self.calculate_statistics()
        statistics_container = self.ids.statistics_container
        if statistics_data:
            for exercise_name, stats in statistics_data.items():
                exercise = OneLineListItem(text=f'Exercise: {exercise_name}',
                                           bg_color=(73 / 255, 67 / 255, 49 / 255, 1))
                statistics_container.add_widget(exercise)

                # Create a single OneLineListItem to display max_kg and max_reps
                max_data = OneLineListItem(
                    text=f'Maximum Kilograms Set: {int(stats["Max Kilograms"])}kg x {int(stats["Max Reps"])}',
                    bg_color=(73 / 255, 67 / 255, 49 / 255, 0.8)
                )
                statistics_container.add_widget(max_data)

                # Add other statistics as needed
                for value in stats:
                    if value not in ["Max Kilograms", "Repetitions with Max Kilograms"]:
                        item = OneLineListItem(text=f'{value}: {int(stats[value])}',
                                               bg_color=(73 / 255, 67 / 255, 49 / 255, 0.8))
                        statistics_container.add_widget(item)

        else:
            item = OneLineListItem(text="No training data available.")
            statistics_container.add_widget(item)

    def go_back_to_menu(self):
        self.ids.statistics_container.clear_widgets()
        self.manager.current = 'menu'

    def go_back_to_menu(self):
        self.ids.statistics_container.clear_widgets()
        self.manager.current = 'menu'

    def calculate_statistics(self, filename='training_data.csv'):
        try:
            df = pd.read_csv(filename)
            if not df.empty:
                statistics_data = {}
                for exercise_name, group in df.groupby('ExerciseName'):
                    max_kg = group['Kilograms'].max()
                    max_reps = group[group['Kilograms'] == max_kg]['Repetitions'].max()
                    mean_kg = group['Kilograms'].mean()
                    mean_reps = group['Repetitions'].mean()
                    total_kgs = group['Kilograms'].sum() * group['Repetitions'].sum()
                    total_reps = group['Repetitions'].sum()
                    count = len(group)
                    statistics_data[exercise_name] = {
                        "Max Kilograms": max_kg,
                        "Max Reps": max_reps,
                        "Mean Kilograms": mean_kg,
                        "Mean Repetitions": mean_reps,
                        "Total Repetitions": total_reps,
                        "Total Kilograms Lifted": total_kgs,
                        "Total Entries": count,
                    }
                return statistics_data
        except FileNotFoundError:
            return None


class MainMenuApp(MDApp):
    font_size = NumericProperty(24)
    background_color = (232 / 255, 232 / 255, 180 / 255, 0.9)
    light_brown = ListProperty((63 / 255, 63 / 255, 55 / 255, 0.6))
    medium_brown = ListProperty((73 / 255, 67 / 255, 49 / 255, 0.8))
    dark_brown = ListProperty((73 / 255, 67 / 255, 49 / 255, 1))
    brown = ListProperty((53 / 255, 42 / 255, 2 / 255, 1))
    brown2 = ListProperty((53 / 255, 42 / 255, 2 / 255, 0.5))
    dark_green = ListProperty((21 / 255, 56 / 255, 44 / 255, 0.96))

    def build(self):
        sm = ScreenManager(transition=SwapTransition())
        menu_screen = MenuScreen(name="menu")
        countdown_screen = CountdownScreen(name="countdown")
        start_screen = StartScreen(name="start")
        last_training_screen = LastTrainingScreen(name="last_training")
        statistics_screen = StatisticsScreen(name="statistics")
        sm.add_widget(menu_screen)
        sm.add_widget(countdown_screen)
        sm.add_widget(start_screen)
        sm.add_widget(last_training_screen)
        sm.add_widget(statistics_screen)
        return sm


if __name__ == "__main__":
    MainMenuApp().run()
