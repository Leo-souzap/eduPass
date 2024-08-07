import flet as ft

def registerPageView(page: ft.Page):
    # Função que será chamada ao clicar no botão "CRIAR CONTA"
    def criar_conta(e):
        # Verifica se todos os campos estão preenchidos
        if not nome.value or not cpf.value or not email.value or not celular.value or not senha.value:
            mensagem.value = "Por favor, preencha todos os campos."
            mensagem.color = "red"
        else:
            mensagem.value = "Cadastro concluído com sucesso!"
            mensagem.color = "green"
        mensagem.update()

    # Criação dos campos de entrada (TextField) para cada dado necessário
    nome = ft.TextField(label="Nome", bgcolor="#ffffff", border_width=2, border_color="#2478ff")
    cpf = ft.TextField(label="CPF", bgcolor="#ffffff", border_width=2, border_color="#2478ff")
    email = ft.TextField(label="Email", bgcolor="#ffffff", border_width=2, border_color="#2478ff")
    celular = ft.TextField(label="Celular", bgcolor="#ffffff", border_width=2, border_color="#2478ff")
    senha = ft.TextField(label="Cadastrar Senha", password=True, can_reveal_password=True, bgcolor="#ffffff", border_width=2, border_color="#2478ff")
    mensagem = ft.Text("")  # Texto para exibir mensagens de feedback para o usuário

    # Retorna uma View contendo todos os elementos da página de registro
    return ft.View(
        "/registerPage",
        [
            # Barra de navegação superior (AppBar) com título e ícone
            ft.AppBar(
                title=ft.Text("Registro", style="headlineSmall", color="#FFFFFF"),
                bgcolor="#FBB927",
                color="#FFFFFF"
            ),
            # Container principal da página
            ft.Container(
                width=page.window.width,
                height=page.window.height,
                bgcolor="#FFFFFF",
                padding=20,
                content=ft.Column(
                    controls=[
                        ft.Text("Olá, Estudante! Informe os seus Dados", style="headlineMedium", color="#22209B"),  # Título da seção
                        nome,
                        cpf,
                        email,
                        celular,
                        senha,
                        mensagem,
                        # Botão para criar conta, que chama a função criar_conta ao ser clicado
                        ft.ElevatedButton("CRIAR CONTA", bgcolor="#FBB927", color="#ffffff", on_click=criar_conta),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    width=400,  # Largura da coluna centralizada
                )
            )
        ]
    )

# Exemplo de como executar a aplicação
if __name__ == "__main__":
    ft.app(target=registerPageView)
