import flet as ft
from database import Database

class RegisterPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()
    
    def criar_conta(self, e):
        nome = self.campo_nome.value
        cpf = self.campo_cpf.value
        email = self.campo_email.value
        celular = self.campo_celular.value
        senha = self.campo_senha.value

        if not nome or not cpf or not email or not celular or not senha:
            self.mensagem.value = "Por favor, preencha todos os campos."
            self.mensagem.color = ft.colors.GREEN
        else:
            self.db.add_student(nome, cpf, email, celular, senha)

            self.mensagem.value = "Cadastro concluído com sucesso!"
            self.mensagem.color = ft.colors.GREEN

            self.mensagem.update()

            self.page.go("/loginPage")
        
        self.mensagem.update()


    def registerPageView(self):
        self.campo_nome = ft.TextField(hint_text="Nome", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_cpf = ft.TextField(hint_text="CPF", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_email = ft.TextField(hint_text="Email", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_celular = ft.TextField(hint_text="Celular", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_senha = ft.TextField(hint_text="Cadastrar Senha", password=True, can_reveal_password=True, bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.mensagem = ft.Text("")

        return ft.View(
            "/registerPage",
            [
                ft.AppBar(
                    leading=ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.1, height=self.page.window.height * 0.1, fit=ft.ImageFit.CONTAIN),
                    bgcolor="#ffffff",
                ),
                # Container principal da página
                ft.Container(
                    width=self.page.window.width,
                    height=self.page.window.height,
                    margin=-10,
                    bgcolor="#ffffff",
                    content=ft.Column(
                        controls=[
                            ft.Text("Olá, Estudante! Informe os seus Dados", style=ft.TextStyle(color="#22209B")),  # Título da seção
                            self.campo_nome,
                            self.campo_cpf,
                            self.campo_email,
                            self.campo_celular,
                            self.campo_senha,
                            self.mensagem,
                            # Botão para criar conta, que chama a função criar_conta ao ser clicado
                            ft.ElevatedButton("CRIAR CONTA", bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE, width=self.page.window.width * 0.8, on_click=self.criar_conta),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=20
                )
            ]
        )


