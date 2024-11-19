from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog

# Tela de Login
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout da tela
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.layout.add_widget(MDLabel(
            text="Login",
            theme_text_color="Secondary",
            halign="center",
            font_style="H4",
            size_hint=(1, 0.1)
        ))

        # Card com campos de login
        login_card = MDCard(
            size_hint=(None, None), size=("300dp", "300dp"), pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=10, radius=[20]
        )
        login_card.add_widget(BoxLayout(orientation='vertical', padding=10, spacing=10))
        
        # Campos de entrada: Usuário e Senha
        self.username_input = MDTextField(
            hint_text="Usuário",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            mode="rectangle",
            line_color_focus=(0, 0, 1, 1),  # Azul para o foco
            required=True
        )
        self.password_input = MDTextField(
            hint_text="Senha",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            mode="rectangle",
            password=True,
            line_color_focus=(0, 0, 1, 1),
            required=True
        )

        login_card.add_widget(self.username_input)
        login_card.add_widget(self.password_input)

        # Botão de login
        login_button = MDRaisedButton(
            text="Entrar",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            pos_hint={"center_x": 0.5},
            md_bg_color=(0, 0.6, 0, 1),  # Verde para o botão
            on_release=self.on_login_click,
            radius=[25]
        )
        
        # Adicionando o botão ao card
        login_card.add_widget(login_button)

        self.layout.add_widget(login_card)

        self.add_widget(self.layout)

    def on_login_click(self, instance):
        # Lógica de autenticação simples
        username = self.username_input.text
        password = self.password_input.text

        if username == "claudio" and password == "XBOX360skyrim":
            self.show_success_dialog()
        else:
            self.show_error_dialog()

    def show_success_dialog(self):
        """Mostra um diálogo de sucesso de login."""
        dialog = MDDialog(
            title="Sucesso",
            text="Login realizado com sucesso!",
            size_hint=(0.8, 0.4)
        )
        dialog.open()

    def show_error_dialog(self):
        """Mostra um diálogo de erro de login."""
        dialog = MDDialog(
            title="Erro",
            text="Usuário ou senha incorretos.",
            size_hint=(0.8, 0.4)
        )
        dialog.open()

class MyApp(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
