import flet as ft

def loginPageView(page: ft.Page):
    return ft.View(
        "/loginPage",
        controls=[
            ft.Container(
                width=page.window.width,
                height=page.window.height,
                margin=-10,
                bgcolor="#ffffff",
                content=ft.Column(
                    controls=[
                        ft.Image(src="../assets/Logo.png", width=150, height=150, fit=ft.ImageFit.CONTAIN),
                        ft.TextField(
                            hint_text="Email ou CPF",
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            border_width=0,
                        ),
                        ft.TextField(
                            hint_text="Senha",
                            password=True,
                            can_reveal_password=True,
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            border_width=0,
                        ),
                        ft.ElevatedButton(
                            text="ACESSAR",
                            bgcolor=ft.colors.ORANGE,
                            color=ft.colors.WHITE,
                            width=page.window.width * 0.8,
                            on_click=lambda _: page.go("/mainPage")
                        ),
                        ft.TextButton(
                            text="Cadastre-se aqui",
                            on_click=lambda _: page.go("/registerPage")
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