from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
 
class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        solution = TextInput(multiline=False)
        main_layout.add_widget(solution)
        solution2 = TextInput(multiline=False)
        main_layout.add_widget(solution2)
        equals_button = Button(text="Сложить")
        equals_button.bind(on_press=lambda instanse: setattr(label1, "text", str(float(solution.text) + float(solution2.text))))
        label1 = Label()
        main_layout.add_widget(equals_button)
        main_layout.add_widget(label1)
         
        return main_layout
 
     
if __name__ == "__main__":
    app = MainApp()
    app.run()