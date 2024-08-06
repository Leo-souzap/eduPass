import flet as ft

def registerPageView(page: ft.Page):
    return ft.View(
        "/registerPage",
        [
            ft.AppBar(
                leading=ft.Icon(ft.icons.ACCOUNT_CIRCLE), 
                title=ft.Text("Registro"), 
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
                            ft.TextField(hint_text="Nome", bgcolor="#ffffff", border_width=2, border_color="#2478ff"),
                            ft.TextField(hint_text="Email", bgcolor="#ffffff", border_width=2, border_color="#2478ff"),
                            ft.TextField(hint_text="Senha", bgcolor="#ffffff", border_width=2, border_color="#2478ff"),
                            ft.ElevatedButton(
                                text="Registrar", 
                                bgcolor="#2478ff", 
                                color="#ffffff", 
                                on_click=lambda _: page.go("/loginPage")
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
