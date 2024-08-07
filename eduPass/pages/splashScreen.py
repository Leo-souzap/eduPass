import flet as ft

def splashScreenView(page: ft.Page):
    return ft.View(
        "/splash",
        [
            # Stack para sobreposição de elementos
            ft.Stack(
                [
                    # Container para o fundo da splash screen
                    ft.Container(
                        width=page.window.width,  # Largura da tela
                        height=page.window.height,  # Altura da tela
                        alignment=ft.alignment.center,  # Alinhamento central
                        content=ft.Column(
                            [
                                # Logo centralizada
                                ft.Image(
                                    src="../assets/Logo.png",
                                    fit=ft.ImageFit.CONTAIN,  # Ajusta a imagem dentro do container
                                    width=page.window.width * 0.6,  # Largura da imagem
                                    height=page.window.height * 0.6,  # Altura da imagem
                                ),
                                # Barra de progresso (comentada)
                                # ft.ProgressBar(width=200, color="#ffffff", value=0.5),  
                            ],
                            alignment="center",  # Alinha o conteúdo da coluna ao centro
                            spacing=10,  # Espaçamento entre a imagem e a barra de progresso
                        ),
                    ),
                ],
            )
        ],
    )
