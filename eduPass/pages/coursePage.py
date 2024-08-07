import flet as ft
from database import Database

class CoursePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def inserir_curso(self, e):
        aluno_id = self.page.session.get("aluno_id")
        print(aluno_id)
        escolaridade = self.campo_escolaridade.value
        unidade = self.campo_unidade.value
        curso = self.campo_curso.value
        turno = self.campo_turno.value
        frequencia = self.campo_frequencia.value

        if not aluno_id or not escolaridade or not unidade or not curso or not turno or not frequencia:
            print("Teste")
            self.mensagem.value = "Por favor, preencha todos os campos."
            self.mensagem.color = ft.colors.RED
            self.mensagem.update()
        else:
            self.db.add_course(escolaridade, unidade, curso, turno, frequencia, "analise", "", aluno_id)

            self.page.go("/menuPage")

    def coursePageView(self):
        self.campo_escolaridade = ft.TextField(hint_text="Nível de Escolaridade", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_unidade = ft.TextField(hint_text="Unidade de Ensino", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_curso = ft.TextField(hint_text="Curso", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_turno = ft.TextField(hint_text="Turno", bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.campo_frequencia = ft.TextField(hint_text="Frequência Mensal", password=True, can_reveal_password=True, bgcolor=ft.colors.GREY,border_radius=10, border_width=0)
        self.mensagem = ft.Text("")

        return ft.View(
            "/coursePage",
            [
                ft.Container(
                    height=40,
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
                    padding=ft.padding.all(10)  # Adiciona padding para melhor visualização
                ),
                ft.Container(
                    width=self.page.window.width,
                    height=self.page.window.height,
                    margin=-10,
                    bgcolor="#ffffff",
                    padding=20,
                    content=ft.Column(
                        controls=[
                            ft.Text("Olá, Estudante! Adicionar Curso", style=ft.TextStyle(color="#22209B")),  # Título da seção
                            self.campo_escolaridade,
                            self.campo_unidade,
                            self.campo_curso,
                            self.campo_turno,
                            self.campo_frequencia,
                            self.mensagem,
                            # Botão para criar conta, que chama a função criar_conta ao ser clicado
                            ft.ElevatedButton("Adicionar Curso", bgcolor=ft.colors.ORANGE, color=ft.colors.WHITE, width=self.page.window.width * 0.8, on_click=self.inserir_curso),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                )
            ]
        )