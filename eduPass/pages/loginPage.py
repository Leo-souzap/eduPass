import flet as ft
from database import Database

class LoginPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def on_login_click(self, e):
        usuario = self.campo_usuario.value
        senha = self.campo_senha.value

        if not usuario or not senha:
            self.mensagem.value = "Por favor, preencha todos os campos."
            self.mensagem.color = ft.colors.RED
            self.mensagem.update()
        else:
            if self.db.verify_login(usuario, senha):
                self.page.go("/menuPage")
            else:
                self.mensagem.value = "Email ou senha estão incorretos, digite novamente."
                self.mensagem.color = ft.colors.GREEN

            self.mensagem.update()

    def loginPageView(self):
        self.campo_usuario = ft.TextField(hint_text="Digite seu email", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_senha = ft.TextField(hint_text="Digite sua senha", password=True, can_reveal_password=True, bgcolor=ft.colors.GREY, border_radius=10, border_width=0)
        self.mensagem = ft.Text("")

        return ft.View(
            "/loginPage",
            controls=[
                ft.Container(
                    width=self.page.window.width,
                    height=self.page.window.height,
                    margin=-10,
                    bgcolor="#ffffff",
                    content=ft.Column(
                        controls=[
                            ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.3, height=self.page.window.height * 0.3, fit=ft.ImageFit.CONTAIN),
                            self.campo_usuario,
                            self.campo_senha,
                            self.mensagem,
                            ft.ElevatedButton(
                                text="ACESSAR",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                width=self.page.window.width * 0.8,
                                on_click= self.on_login_click
                            ),
                            ft.TextButton(
                                text="Cadastre-se aqui",
                                on_click=lambda _: self.page.go("/registerPage")
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=20
                ),
            ]
        )

