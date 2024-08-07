import flet as ft

def menuPageView(page: ft.Page):
    def create_button(text, route):
        return ft.Container(
            content=ft.ElevatedButton(
                text=text,
                width=120,
                height=120,
                bgcolor="#E4E4E2",
                color="#000000",
                on_click=lambda _: page.go(route)
            ),
            width=120,
            height=120,
            # border_radius=10,  # Borda arredondada
            alignment=ft.alignment.center,
            # margin=0,  # Reduzir margem
        )

    return ft.View(
        "/menuPage",
        [
            ft.Container(
                # width=page.window.width,
                # height=page.window.height,
                bgcolor="#FFFFFF",
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Image(src="../assets/Logo.png", width=80, height=40),
                                ft.TextButton("Sair", on_click=lambda _: page.go("/loginPage"), style=ft.ButtonStyle(color="#888888")),
                            ],
                            alignment="spaceBetween",
                        ),
                        # ft.Container(height=10),  # Espaçamento vertical acima do texto
                        ft.Text(
                            "Olá, Estudante!\nO que deseja fazer?",
                            size=20,
                            color="#888888",
                            text_align="center",
                            width=page.window.width,  # Define a largura para centralizar o texto
                        ),
                        ft.Container(height=10),  # Espaçamento vertical acima dos botões
                        ft.Row(
                            [
                                create_button("Perfil", "/profilePage"),
                                create_button("Curso", "/coursePage"),
                            ],
                            alignment="center",
                            # spacing=20,  # Reduzir espaçamento entre botões
                        ),
                        ft.Container(height=10),  # Espaçamento vertical entre linhas de botões
                        ft.Row(
                            [
                                create_button("Doc", "/documentsPage"),
                                create_button("Status", "/statusPage"),
                            ],
                            alignment="center",
                            # spacing=20,  # Reduzir espaçamento entre botões
                        ),
                    ],
                    alignment="center",  # Centraliza o conteúdo da coluna
                    # spacing=10,  # Espaçamento vertical entre os elementos da coluna
                ),
            )
        ],
    )
