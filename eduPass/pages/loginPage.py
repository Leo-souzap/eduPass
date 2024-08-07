import flet as ft

def loginPageView(page: ft.Page):
    return ft.View(
        "/loginPage",
        [
            ft.AppBar(
                leading=ft.Icon(ft.icons.TASK),
                title=ft.Text("Gerenciador de Tarefas"),
                bgcolor="#2478ff",
                color="#ffffff"
            ),
            ft.Container(
                width=page.window.width,
                height=page.window.height,
                margin=-10,
                bgcolor="#ffffff",
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.TextField(
                                hint_text="Usuário",
                                bgcolor="#ffffff",
                                border_width=2,
                                border_color="#2478ff"
                            ),
                            ft.TextField(
                                hint_text="Senha",
                                bgcolor="#ffffff",
                                border_width=2,
                                border_color="#2478ff"
                            ),
                            ft.ElevatedButton(
                                text="Fazer Login",
                                bgcolor="#2478ff",
                                color="#ffffff",
                                on_click=lambda _: page.go("/menuPage")  # Redireciona para a página de menu
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    padding=20
                )
            ),
        ]
    )
