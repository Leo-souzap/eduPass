import flet as ft
from pages.loginPage import loginPageView
from pages.registerPage import registerPageView
from pages.splashScreen import splashScreenView
from pages.menuPage import menuPageView
from pages.profilePage import profilePageView
from pages.coursePage import coursePageView
from pages.documentsPage import documentsPageView
from pages.statusPage import statusPageView
import threading

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "EduPass"
    page.window.width = 800
    page.window.height = 600
    page.bgcolor = "#FFFFFF"
    
    def route_change(route):
        # Limpa e atualiza a visualização com base na rota
        page.views.clear()
        if page.route == "/splash":
            page.views.append(splashScreenView(page))
        elif page.route == "/loginPage":
            page.views.append(loginPageView(page))
        elif page.route == "/registerPage":
            page.views.append(registerPageView(page))
        elif page.route == "/menuPage":
            page.views.append(menuPageView(page))
        elif page.route == "/profilePage":
            page.views.append(profilePageView(page))
        elif page.route == "/coursePage":
            page.views.append(coursePageView(page))
        elif page.route == "/documentsPage":
            page.views.append(documentsPageView(page))
        elif page.route == "/statusPage":
            page.views.append(statusPageView(page))
        page.update()  # Atualiza a página

    page.on_route_change = route_change  # Define a função de mudança de rota
    page.go("/splash")  # Inicialmente vai para a página de splash

    def switch_to_login():
        # Navega para a página de login após o timer
        page.go("/loginPage")

    def start_timer():
        # Inicia um timer para mudar para a página de login após 3 segundos
        threading.Timer(3.0, switch_to_login).start()

    start_timer()  # Começa o timer

ft.app(target=main)
