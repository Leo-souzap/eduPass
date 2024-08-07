import flet as ft

def profilePageView(page: ft.Page):
    return ft.View(
        "/profilePage",
        [
            ft.Container(
                bgcolor="#FFFFFF",
                padding=20,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Image(src="../assets/Logo.png", width=80, height=40),
                                ft.TextButton("Menu", on_click=lambda _: page.go("/menuPage"), style=ft.ButtonStyle(color="#888888")),
                            ],
                            alignment="spaceBetween",
                        ),
                        ft.Text(
                            "Perfil",
                            size=24,
                            color="#888888",
                            text_align="center",
                            width=page.window.width,  # Define a largura para centralizar o texto
                        ),
                        # Conteúdo da página de Perfil
                        ft.Container(
                            # Adicione seu conteúdo aqui
                        ),
                        ft.Container(height=10),  # Espaçamento vertical acima do botão de voltar
                        # O botão "Menu" já está no topo da página
                    ],
                    alignment="center",
                ),
            )
        ],
    )
