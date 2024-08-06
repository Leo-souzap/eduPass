import flet as ft
import pages.loginPage as loginPageView
import pages.registerPage as registerPageView

def splash_screen(page: ft.Page):
    page.title = "EduPass"
    page.bgcolor = ft.colors.WHITE
    logo = ft.Image(src="../assets/Logo.png", width=200, height=200)
    btn_vai = ft.ElevatedButton(text="Vai", bgcolor=ft.colors.GREEN, color=ft.colors.BLACK, on_click=lambda _: page.go("/loginPage"))
    page.add(
        ft.Column(
            [
                ft.Row(
                    [logo, btn_vai],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
    )
    page.update()


def route_change(page: ft.Page):
    page.views.clear()
    if page.route == "/":
        splash_screen(page)
    elif page.route == "/loginPage":
        page.views.append(loginPageView(page))
    elif page.route == "/registerPage":
        page.views.append(registerPageView(page))
    page.update()

def view_pop(page: ft.Page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)

def main(page: ft.Page):
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
ft.app(target=main)
