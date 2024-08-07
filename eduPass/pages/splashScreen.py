import flet as ft

def splashScreenView(page: ft.Page):
    return ft.View(
        "/splash",
        controls=[
            ft.Container(
                width=page.window.width,
                height=page.window.height,
                bgcolor="#ffffff",
                content=ft.Column(
                    controls=[
                        ft.Image(src="../assets/Logo.png", width=page.window.width * 0.3, height=page.window.width * 0.3, fit=ft.ImageFit.CONTAIN)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
            )
        ],
    )
