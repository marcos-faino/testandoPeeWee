import kivy
from kivy.app import App
from gerencTelas import GerenciaTelas

kivy.require('2.0.0')

__version__ = "0.2"


class exemploCrud(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root


if __name__ == '__main__':
    exemploCrud().run()
