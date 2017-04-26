#!/usr/bin/env python2

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.button import Button

button = Button(pos=(300,300),font_size=20)
textinput= TextInput(text='Hello world',multiline=False)

def on_text(self, *args):
        print ('new value is ', textinput.text)
        Clipboard.put(textinput.text,'UTF8_STRING')
        button.text= Clipboard.get('UTF8_STRING')
        self.add_widget(button)

class MyClipBoardApp(App):
    def build(self):
        root= GridLayout()
        layout = FloatLayout(orientation='horizontal', size=(450,300), size_hint=(None, None))
        #call function when text changes inside TextInput
        textinput.bind(text=on_text)
        print ('value is ', textinput.text)
        print(Clipboard.put(textinput.text,'UTF8_STRING'))
        print(Clipboard.get('UTF8_STRING'))
        #Use copied clipboard value as text for Button
        button.text= Clipboard.get('UTF8_STRING')
        layout.add_widget(button)
        layout.add_widget(textinput)
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    MyClipBoardApp().run()
