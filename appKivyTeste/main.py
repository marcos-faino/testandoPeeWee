# import kivy module
import kivy

from kivy.app import App
from kivy.uix.popup import Popup

kivy.require('1.11.0')

# Widgets são elementos
# de uma interface gráfica de usuário
from kivy.uix.widget import Widget

# O widget Label provê um
# texto não editável, ou rótulo
from kivy.uix.label import Label

# Criando a classe do widget da tela
class Tela1(Widget):
    pass


# Create the app class

class MainApp(App):
    def build(self):
        return Tela1()

    def somar(self):
        try:
            valor1 = int(self.root.ids.input1.text)
            valor2 = int(self.root.ids.input2.text)
            self.root.ids.result.text = str(valor1 + valor2)
        except:
            popup = Popup(title='Erro', content=Label(text='Você inseriu um valor inválido'), auto_dismiss=True)
            popup.size_hint = (0.98,0.4)
            popup.open()


# Rodando o App
if __name__ == "__main__":
    MainApp().run()