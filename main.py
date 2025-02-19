from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):
    def __init__(self, tarefas=[], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))  # Adiciona tarefas iniciais
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
    
    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
        


    def add_widget_tarefa(self):
        texto = self.ids.texto.text.strip()  # Remove espaços em branco
        if texto:
            self.ids.box.add_widget(Tarefa(text=texto))
            self.ids.texto.text = ''  # Limpa o campo de texto

class Tarefa(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text  # Define o texto na label

class Test(App):
    def build(self):
        return Gerenciador()

Test().run()
