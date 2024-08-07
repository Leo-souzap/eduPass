import flet as ft

def documentsPageView(page: ft.Page):
    return ft.View(
        "/documentsPage",
        [
            # Container principal
            ft.Container(
                bgcolor="#FFFFFF",  # Cor de fundo
                padding=20,  # Padding interno
                content=ft.Column(
                    [
                        # Cabeçalho com logo e botão de menu
                        ft.Row(
                            [
                                ft.Image(src="../assets/Logo.png", width=80, height=40),  # Logo
                                ft.TextButton(
                                    "Menu", 
                                    on_click=lambda _: page.go("/menuPage"),  # Navegação para Menu
                                    style=ft.ButtonStyle(color="#888888")  # Estilo do botão
                                ),
                            ],
                            alignment="spaceBetween",  # Alinhamento dos itens
                        ),
                        # Título centralizado
                        ft.Text(
                            "Documentos",
                            size=24,  # Tamanho da fonte
                            color="#888888",  # Cor do texto
                            text_align="center",  # Alinhamento do texto
                            width=page.window.width,  # Largura para centralizar
                        ),
                        # Container para o conteúdo da página
                        ft.Container(
                            # Adicionar conteúdo aqui
                        ),
                        # Espaço acima do botão de voltar
                        ft.Container(height=10),  # Espaço vertical
                    ],
                    alignment="center",  # Alinhamento dos itens
                ),
            )
        ],
    )
