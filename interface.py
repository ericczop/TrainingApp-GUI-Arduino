import time
import threading
import pandas as pd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivymd.uix.list import OneLineListItem, IconLeftWidget, TwoLineIconListItem
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from connection import Connection
from analysis import start_analysis, calculate_statistics

Builder.load_file('FILES/builder.kv')


class MenuScreen(Screen):

    def start_button_pressed(self):
        self.manager.current = 'countdown'
        data_thread = threading.Thread(target=self.process_data)
        data_thread.start()

    def last_trainings_button_pressed(self):
        self.manager.current = 'last_training'

    def statistics_button_pressed(self):
        self.manager.current = 'statistics'

    def process_data(self):
        kg, reps = start_analysis(connection)
        start_screen = self.manager.get_screen('start')
        start_screen.initialize_data(kg, reps)

    def quit_app(self):
        MDApp.get_running_app().stop()


class CountdownScreen(Screen):
    countdown = NumericProperty(5)
    start_time = NumericProperty(0)
    end_time = NumericProperty(0)

    def on_pre_enter(self):
        self.ids.stop_button.disabled = True
        self.countdown = 5

    def on_enter(self):
        Clock.schedule_interval(self.update_countdown, 1)

    def update_countdown(self, dt):
        self.countdown -= 1
        self.countdown_label.text = f'Start exercising in: {self.countdown}'
        if self.countdown == 0:
            Clock.unschedule(self.update_countdown)
            self.ids.countdown_label.text = '          Click a button\nwhen you finish your set!'
            self.ids.stop_button.disabled = False
            self.start_time = time.time()

    def stop_button_pressed(self):
        connection.stop_providing()
        self.manager.current = 'start'
        self.end_time = time.time()
        duration_time = round(self.end_time - self.start_time, 2)
        start_screen = self.manager.get_screen('start')
        start_screen.duration = duration_time


class StartScreen(Screen):
    kg = NumericProperty(0)
    reps = NumericProperty(0)
    duration = NumericProperty(0)

    def initialize_data(self, kg, reps):
        self.kg = kg
        self.reps = reps
        self.kg_label.text = f'Kilograms loaded: {self.kg}kg'
        self.reps_label.text = f'Number of reps done: {self.reps}'
        self.ids.time_label.text = f'Time of set done: {self.duration}s'
        self.ids.exercise_name_input.disabled = False
        self.ids.save_button.disabled = False

    def process_data(self):
        kg, reps = start_analysis(connection)
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
        self.ids.exercise_name_input.text = ''

    def save_data_to_csv(self, kg, reps, duration, filename='FILES/training_data.csv'):
        exercise_name = self.ids.exercise_name_input.text
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['ExerciseName', 'Kilograms', 'Repetitions', 'Time'])

        new_data = pd.DataFrame(
            {'ExerciseName': [exercise_name], 'Kilograms': [kg], 'Repetitions': [reps], 'Time': [duration]})
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(filename, index=False)

    def save_button_pressed(self):
        self.save_data_to_csv(self.kg, self.reps, self.duration, filename='FILES/training_data.csv')
        self.ids.back_button.disabled = False
        self.ids.next_button.disabled = False
        self.ids.exercise_name_input.disabled = True
        self.ids.save_button.disabled = True


class LastTrainingScreen(Screen):
    first_color = (0.7, 0.7, 0.7, 1)

    def on_pre_enter(self):
        training_names, training_data = self.load_training_data()
        try:
            for _ in range(len(training_data)):
                item = TwoLineIconListItem(IconLeftWidget(icon="dumbbell"),
                                           text=training_names[_], secondary_text=training_data[_])
                item.bg_color = self.first_color
                self.ids.container.add_widget(item)
        except TypeError:
            pass

    def go_back_to_menu(self):
        self.ids.container.clear_widgets()
        self.manager.current = 'menu'

    def load_training_data(self, filename='FILES/training_data.csv'):
        try:
            df = pd.read_csv(filename)
            if not df.empty:
                training_data = []
                training_names = []
                for index, row in df.iterrows():
                    name_entry = f'{row["ExerciseName"]}'
                    data_entry = (f'Kilograms: {row["Kilograms"]} | Repetitions: {row["Repetitions"]} | '
                                  f'Time: {row["Time"]}')
                    training_names.append(name_entry)
                    training_data.append(data_entry)
                return training_names, training_data
        except FileNotFoundError:
            self.ids.container.add_widget(OneLineListItem(text="No training data available."))


class StatisticsScreen(Screen):
    first_color = (0.7, 0.7, 0.7, 1)
    second_color = (0.5, 0.0, 0.1, 1)

    def on_pre_enter(self):
        statistics_data = calculate_statistics()
        statistics_container = self.ids.statistics_container
        if statistics_data:
            for exercise_name, stats in statistics_data.items():
                exercise = OneLineListItem(
                    text=f'{exercise_name}',
                    bg_color=self.second_color,
                    text_color=self.first_color,
                    theme_text_color="Custom")
                statistics_container.add_widget(exercise)

                max_data = TwoLineIconListItem(
                    IconLeftWidget(icon="poll"),
                    text='Maximum Kilograms Set',
                    secondary_text=f'{stats["Max Kilograms"]}kg x {stats["Max Repetitions"]}',
                    bg_color=self.first_color
                )
                statistics_container.add_widget(max_data)

                for value in stats:
                    if value not in ["Max Kilograms", "Repetitions with Max Kilograms"]:
                        item = TwoLineIconListItem(
                            IconLeftWidget(icon="poll"),
                            text=f'{value}:',
                            secondary_text=f'{stats[value]}',
                            bg_color=self.first_color)
                        statistics_container.add_widget(item)

        else:
            item = OneLineListItem(text="No training data available.")
            statistics_container.add_widget(item)

    def go_back_to_menu(self):
        self.ids.statistics_container.clear_widgets()
        self.manager.current = 'menu'


class TrainingAppApp(MDApp):
    font_size = NumericProperty(24)
    button_size = NumericProperty(40)

    background = (0.1, 0.1, 0.1, 1)
    button_color = (0.7, 0.7, 0.7, 1)
    icon_color = (0.5, 0.0, 0.1, 1)
    stop_color = (0.91, 0.15, 0.21, 1)
    dark_green = (21 / 255, 56 / 255, 44 / 255, 0.96)
    additional_color = (0.15, 0.15, 0.15, 1)
    additional_color2 = (0.25, 0.25, 0.25, 1)
    additional_color3 = (0.35, 0.35, 0.35, 1)
    additional_color4 = (0.5, 0.5, 0.5, 1)

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
    connection = Connection("COM3")
    TrainingAppApp().run()
