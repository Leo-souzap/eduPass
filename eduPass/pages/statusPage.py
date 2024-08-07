import flet as ft
from database import Database

class StatusPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def get_course_info(self):
        aluno_id = self.page.session.get("aluno_id")
        course_info = self.db.get_course_info(aluno_id)
        print(course_info)
        return course_info

    def statusPageView(self):
        ft.Container(
            height=40,
            content=ft.Row(
                [
                    ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.1, height=80, fit=ft.ImageFit.CONTAIN),
                    ft.TextButton(
                        "Sair", 
                        on_click=lambda _: self.page.go("/loginPage"),  # Navega para a página de login
                        style=ft.ButtonStyle(color="#888888")  # Estilo do botão
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Espaça os elementos igualmente
            ),
            bgcolor="#ffffff",
        ),

        course_info = self.get_course_info()


        if course_info:
            tipo, unidade, curso, turno, frequencia, aprovado, comentario = course_info
            
            return ft.View(
                "/profilePage",
                [
                    ft.Container(
                        margin=-10,
                        content=ft.Row(
                            [
                                ft.Image(src="../assets/Logo.png", width=self.page.window.width * 0.1, height=80, fit=ft.ImageFit.CONTAIN),
                                ft.TextButton(
                                    "Voltar", 
                                    on_click=lambda _: self.page.go("/menuPage"),  # Navega para a página de login
                                    style=ft.ButtonStyle(color="#888888")  # Estilo do botão
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Espaça os elementos igualmente
                        ),
                        bgcolor="#ffffff",
                    ),
                    ft.Container(
                        width=self.page.window.width,
                        height=self.page.window.height,
                        margin=-10,
                        bgcolor="#ffffff",
                        content=ft.Column(
                            [
                                ft.Image(src="../assets/joinha.jpg", height = 100, width=100),
                                ft.Text("Status do cadastro do curso:", size=24, weight="bolder", color="#22209B"),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(f"Nivel Escolaridade: {tipo}", weight="light", size=20, color="#333333"),
                                            ft.Text(f"Unidade de ensino: {unidade}",  weight="light",size=20, color="#333333"),
                                            ft.Text(f"Curso: {curso}",  weight="light",size=20, color="#333333"),
                                            ft.Text(f"Turno: {turno}",  weight="light",size=20, color="#333333"),
                                            ft.Text(f"Frequencia Semanal: {frequencia}",  weight="light",size=20, color="#333333"),
                                            ft.Text(f"Status: {aprovado}",  weight="light",size=20, color="#333333"),
                                            ft.Text(f"Comentario: {comentario}",  weight="light",size=20, color="#333333"),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        horizontal_alignment=ft.CrossAxisAlignment.START,
                                        spacing=10,
                                    ),
                                    border_radius=10,
                                    border={"top": ft.BorderSide(1, color="#CCCCCC"),
                                            "right": ft.BorderSide(1, color="#CCCCCC"),
                                            "bottom": ft.BorderSide(1, color="#CCCCCC"),
                                            "left": ft.BorderSide(1, color="#CCCCCC")},
                                    padding=20,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                        padding=20
                    )
                ]
            )
        else: 
            return ft.View(
                "/statusPage",
                [
                    ft.Text("Erro ao carregar informações do curso.", size=20, color="red")
                ]
            )
