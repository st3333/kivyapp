from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput    
from kivy.uix.boxlayout import BoxLayout    
from kivy.uix.popup import Popup

class helloapp(App):
    def build(self):
        self.bl = BoxLayout(orientation='vertical', size_hint=(0.8, 0.8))
        self.label = Label(text='Enter your name:')
        self.ti = TextInput(hint_text='Enter your name')
        self.btn = Button(text='Greet', on_press=self.show_popup)
        self.bl.add_widget(self.label)
        self.bl.add_widget(self.ti)
        self.bl.add_widget(self.btn)
        return self.bl

    def close_popup(self, instance):
        instance.parent.parent.dismiss()

    def show_popup(self, instance):
        name = self.ti.text
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f'Hello, {name}!'))
        close_btn = Button(text='Close', on_press=self.close_popup)
        content.add_widget(close_btn)
        popup = Popup(title='Hello', content=content, size_hint=(0.5, 0.5))
        popup.open()

if __name__ == '__main__':
    helloapp().run()