import flet as ft
from database import Database

class SplashScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def splashScreenView(self):
        return ft.View(
            "/splash",
            controls=[
                ft.Container(
                    width=self.page.window.width,
                    height=self.page.window.height,
                    margin=-10,
                    bgcolor="#ffffff",
                    content=ft.Column(
                        controls=[
                            ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.3, height=self.page.window.width * 0.3, fit=ft.ImageFit.CONTAIN)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                )
            ],
        )
