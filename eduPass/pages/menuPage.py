import flet as ft

class MenuPage:
    def __init__(self, page: ft.Page):
            self.page = page

    def menuPageView(self):
        def create_button(text, route):
            # Cria um botão com texto e ação de navegação
            return ft.Container(
                content=ft.ElevatedButton(
                    text=text,
                    width=120,
                    height=120,
                    bgcolor="#E4E4E2",  # Cor de fundo do botão
                    color="#000000",  # Cor do texto
                    on_click=lambda _: self.page.go(route)  # Navega para a rota especificada
                ),
                width=120,
                height=120,
                alignment=ft.alignment.center,  # Alinha o botão ao centro
            )

        return ft.View(
            "/menuPage",
            [
                ft.Container(
                    height=40,
                    content=ft.Row(
                        [
                            ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.1, height=80, fit=ft.ImageFit.CONTAIN),
                            ft.TextButton(
                                "Sair", 
                                on_click=lambda _: self.page.go("/loginPage"),  # Navega para a página de login
                                style=ft.ButtonStyle(color="#888888")  # Estilo do botão
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Espaça os elementos igualmente
                    ),
                    bgcolor="#ffffff",
                    padding=ft.padding.all(10)  # Adiciona padding para melhor visualização
                ),
                # Container principal da página
                ft.Container(
                    width=self.page.window.width,
                    height=self.page.window.height,
                    margin=-10,
                    bgcolor="#ffffff",
                    content=ft.Column(
                        [
                            # Texto de boas-vindas
                            ft.Text(
                                "Olá, Estudante!\nO que deseja fazer?",
                                size=20,  # Tamanho da fonte
                                color="#888888",  # Cor do texto
                                text_align="center",  # Alinhamento do texto
                                width=self.page.window.width,  # Largura para centralizar o texto
                            ),
                            # Linha de botões
                            ft.Row(
                                [
                                    create_button("Perfil", "/profilePage"),
                                    create_button("Curso", "/coursePage"),
                                ],
                                alignment="center",  # Alinhamento dos botões
                            ),
                            # Espaço entre linhas de botões
                            ft.Container(height=10),
                            # Linha de botões
                            ft.Row(
                                [
                                    create_button("Doc", "/documentsPage"),
                                    create_button("Status", "/statusPage"),
                                ],
                                alignment="center",  # Alinhamento dos botões
                            ),
                        ],
                        alignment="center",  # Alinhamento vertical dos elementos
                    ),
                    padding=20
                )
            ],
        )