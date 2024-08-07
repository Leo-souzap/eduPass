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
    page.title = "EduPass"
    page.window.width = 800
    page.window.height = 600
    page.bgcolor = "#FFFFFF"
    
    def route_change(route):
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
        # Nenhuma página padrão ou fallback para exibir
        page.update()
    
    page.on_route_change = route_change
    page.go("/splash")

    def switch_to_login():
        page.go("/loginPage")

    def start_timer():
        threading.Timer(3.0, switch_to_login).start()

    start_timer()

ft.app(target=main)
