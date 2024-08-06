import flet as ft

def loginPageView(page: ft.Page):
    return ft.View(
        "/loginPage",
        [
            #Header com o titulo da pagina
            ft.AppBar(leading=ft.Icon(ft.icons.TASK), title=ft.Text("Gerenciador de Tarefas"), bgcolor="#2478ff", color="#ffffff"),
            
            #Container principal
            ft.Container(
                width=page.window.width,
                height=page.window.height,
                margin=-10,
                bgcolor = "#ffffff",
                #Código responsável por definir a pagina com a cor degrade
                #gradient=ft.LinearGradient(
                #    colors=["#8d092d","#ffffff"],
                #    begin=ft.Alignment(-1,-1),
                #    end=ft.Alignment(1,1)
                #),
                #Container com os textos e inputs
                content=ft.Container(
                    #Column responsável por deixar os inputs de Usuário e senha, e o botão de logar um abaixo do outro
                    content=ft.Column(
                    controls=[
                        #Campo de texto do usuário
                        ft.TextField(hint_text="Usuário", bgcolor = "#ffffff", border_width = 2, border_color = "#2478ff"),
                        #Campo de texto da senha
                        ft.TextField(hint_text="Senha", bgcolor = "#ffffff", border_width = 2, border_color = "#2478ff"),
                        #Botão de logar, responsável por redirecionar para a pagina principal, onde se pode visualizar as tarefas
                        ft.ElevatedButton(
                            text="Fazer Login", 
                            bgcolor = "#2478ff", 
                            color = "#ffffff", 
                            on_click=lambda _: page.go("/mainPage")
                        ),
                    ],
                    #Centralizando o container no centro
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20
            )
            ),
        ]
    )