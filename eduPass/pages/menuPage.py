import flet as ft

def menuPageView(page: ft.Page):
    def create_button(text, route):
        # Cria um botão com texto e ação de navegação
        return ft.Container(
            content=ft.ElevatedButton(
                text=text,
                width=120,
                height=120,
                bgcolor="#E4E4E2",  # Cor de fundo do botão
                color="#000000",  # Cor do texto
                on_click=lambda _: page.go(route)  # Navega para a rota especificada
            ),
            width=120,
            height=120,
            alignment=ft.alignment.center,  # Alinha o botão ao centro
        )

    return ft.View(
        "/menuPage",
        [
            # Container principal da página
            ft.Container(
                bgcolor="#FFFFFF",  # Cor de fundo da página
                content=ft.Column(
                    [
                        # Cabeçalho com logo e botão de sair
                        ft.Row(
                            [
                                ft.Image(src="../assets/Logo.png", width=80, height=40),  # Logo
                                ft.TextButton(
                                    "Sair", 
                                    on_click=lambda _: page.go("/loginPage"),  # Navega para a página de login
                                    style=ft.ButtonStyle(color="#888888")  # Estilo do botão
                                ),
                            ],
                            alignment="spaceBetween",  # Alinhamento dos itens
                        ),
                        # Texto de boas-vindas
                        ft.Text(
                            "Olá, Estudante!\nO que deseja fazer?",
                            size=20,  # Tamanho da fonte
                            color="#888888",  # Cor do texto
                            text_align="center",  # Alinhamento do texto
                            width=page.window.width,  # Largura para centralizar o texto
                        ),
                        # Espaço acima dos botões
                        ft.Container(height=10),  
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
            )
        ],
    )
