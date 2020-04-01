import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import  TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Name"))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name"))
        self.last = TextInput(multiline=False)
        self.inside.add_widget(self.last)

        self.inside.add_widget(Label(text="Adresse"))
        self.adr = TextInput()
        self.inside.add_widget(self.adr)


        self.add_widget(self.inside)
        self.submit = Button(text="submit", font_size=40)
        self.submit.bind(on_press= self.prss)
        self.add_widget(self.submit)

    def prss(self, instance):
        print("pressed")
        Name = self.name.text
        Last = self.last.text
        adresse = self.adr.text
        print ("Name:", Name, "last name:", Last, "adresse:", adresse)
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()