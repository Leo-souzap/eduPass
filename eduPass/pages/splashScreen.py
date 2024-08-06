import flet as ft

def splashScreenView(page: ft.Page):
    return ft.View(
        "/splash",
        [
            ft.Stack(
                [
                    ft.Container(
                        width=page.window.width,
                        height=page.window.height,
                        content=ft.Image(
                            src="../assets/Logo.png",
                            fit=ft.ImageFit.CONTAIN,
                            width=page.window.width * 0.6,
                            height=page.window.height * 0.6, 
                        ),
                    ),
                    ft.Container(
                        width=page.window.width,
                        height=page.window.height,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [
                                # ft.Text(
                                #     "EduPass",
                                #     size=50,
                                #     weight=ft.FontWeight.BOLD,
                                #     color="black",
                                # ),
                                ft.ProgressBar(width=200, color="#ffffff", value=0.5),  
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                    ),
                ],
            )
        ],
    )
