import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class Mygrid(GridLayout):
    def __init__(self,**kwargs):
        super(Mygrid,self).__init__(**kwargs)
        self.cols=1
        self.add_widget(Label(text="First Name:"))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text="Last Name:"))
        self.lastname=TextInput(multiline=False)
        self.add_widget(self.lastname)

class MyApp(App):
    def build(self):
        return Mygrid()

if __name__=="__main__":
    MyApp().run()
