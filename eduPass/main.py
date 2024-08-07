import flet as ft
from pages.splashScreen import SplashScreen
from pages.loginPage import LoginPage
from pages.registerPage import RegisterPage
from pages.menuPage import MenuPage
from pages.coursePage import CoursePage
from pages.profilePage import ProfilePage
import threading

def main(page: ft.Page):

    page.title = "EduPass"
    page.window.width = 800 
    page.window.height = 800
    page.bgcolor = "#FFFFFF"

    splash_screen = SplashScreen(page)
    login_page  = LoginPage(page)
    register_page  = RegisterPage(page)
    menu_page  = MenuPage(page)
    course_page  = CoursePage(page)
    profile_page = ProfilePage(page)
    
    
    # Definindo a função de mudança de rota
    def route_change(route):
        page.views.clear()
        if page.route == "/splash":
            page.views.append(splash_screen.splashScreenView())
        elif page.route == "/loginPage":
            page.views.append(login_page.loginPageView())
        elif page.route == "/registerPage":
            page.views.append(register_page.registerPageView())
        elif page.route == "/menuPage":
            page.views.append(menu_page.menuPageView())
        elif page.route == "/coursePage":
            page.views.append(course_page.coursePageView())
        elif page.route == "/profilePage":
            page.views.append(profile_page.profilePageView())
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
