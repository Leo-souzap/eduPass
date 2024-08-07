import flet as ft
from pages.loginPage import loginPageView
from pages.registerPage import registerPageView
from pages.splashScreen import SplashScreen
import threading

def main(page: ft.Page):
    # Configurações da janela
    page.title = "EduPass"
    page.window.width = 800  # Atualizado aqui
    page.window.height = 600  # Atualizado aqui
    page.bgcolor = "#FFFFFF"

    splash_screen = SplashScreen(page)
    
    # Definindo a função de mudança de rota
    def route_change(route):
        page.views.clear()
        if page.route == "/splash":
            page.views.append(splash_screen.splashScreenView())
        elif page.route == "/loginPage":
            page.views.append(loginPageView(page))
        elif page.route == "/registerPage":
            page.views.append(registerPageView(page))
        else:
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("EduPass")),
                        ft.ElevatedButton(text="Ir para Login", on_click=lambda _: page.go("/loginPage")),
                        ft.ElevatedButton(text="Ir para Registro", on_click=lambda _: page.go("/registerPage")),
                    ],
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go("/splash")

    # Configura o temporizador para a tela de splash
    def switch_to_login():
        page.go("/loginPage")

    def start_timer():
        threading.Timer(3.0, switch_to_login).start()

    start_timer()

ft.app(target=main)
