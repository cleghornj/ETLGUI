import pandas as pd
import io
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import scale
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        layout = BoxLayout(orientation='vertical')
        self.dropdown = DropDown()
        self.mainbutton = Button(text='Fields', size_hint=(None, None))
        self.label = Label(text="Drop a CSV to view")
        layout.add_widget(self.label)
        layout.add_widget(self.dropdown)
        layout.add_widget(self.mainbutton)

        return layout

    def _on_file_drop(self, window, file_path):
        print(file_path)
        df = pd.read_csv(file_path.decode("utf-8"))
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', -1)
        self.label.text = str(df.head(5))
        fields = list(df.columns)
        print(fields)
        for field in fields:
            btn = Button(text='Value %s' % field, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        self.mainbutton.bind(on_release=self.dropdown.open)
       # with Window.canvas:
           # Rectangle(color="red", pos=(0, 100), size=(500, 50), text=file_path)
        return


if __name__ == '__main__':
    WindowFileDropExampleApp().run()
