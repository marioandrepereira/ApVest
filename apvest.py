import os
import PySimpleGUI as sg

sobre ='''
ApVest

Version: 2.1.1
Date: 2023-01-26

Criado por:
Jamisson Luis & Mário André
****   e-mail   ****
// jamisson.graca@redeinspiraeducadores.com.br 
// mario.pereira@redeinspiraeducadores.com.br 
'''
# Layout
sg.theme('DarkTeal9')

WIN_W: int = 90
WIN_H: int = 25

# Variáveis ​​de string para reduzir o loop e o código do menu!
cadastro: str = "Cadastrar_Alunos"
lista: str = "Lista_de_Aprovados"
pesquisar: str = "Consultar_Aprovados"
exibir: str = "Alunos"
version = "ApVest Version 2.1.1"

#busca
file_path = "alunos.txt"
file_path2 = "lista.txt"

# Menu
menu_layout: list = [
    ["Exibir", ["Alunos"]],
    ["Cadastro", [cadastro, lista, "---", "Exit"]],
    ["Ferramentas ",[pesquisar]],
    ["Ajuda", ["Sobre"]],
]

layout: list = [
    [sg.Menu(menu_layout)],
    [sg.Text("", font=("Consolas", 10), size=(WIN_W, 1), key="_INFO_")],
    [sg.Image('logo.png', WIN_W, WIN_H, pad=(250,0))]
]

window: object = sg.Window(version, layout, margins=(50, 50), resizable=True)

def alunos(): 
    import os
    layout1 = [
       [sg.Text('Insira os nome dos Alunos.')],
       [sg.Multiline(size=(WIN_W, WIN_H), key="_alunos_")],
       [sg.Button('Salvar'),sg.Button('Exit')]
    ]

    janela1 = sg.Window(version, layout1)

    while True:
        eventos, valores = janela1.read()
        if eventos == 'Salvar':
            with open("alunos.txt", "w") as f:
                f.write(valores['_alunos_'])
                janela1.close()
                break
        elif eventos == sg.WIN_CLOSED or eventos == 'Exit':
            janela1.close()
            break


def listas(): 
    layout2 = [
        [sg.Text('Insira os nomes da lista dos aprovados.')],
        [sg.Multiline(size=(WIN_W, WIN_H), key="_lista_")],
        [sg.Button('Salvar'),sg.Button('Exit')]
    ]

    janela2 = sg.Window(version, layout2)

    while True:
        eventos, valores = janela2.read()
        if eventos == 'Salvar':
            with open("lista.txt", "w") as f:
                f.write(valores['_lista_'])
                break
        elif eventos == sg.WIN_CLOSED or eventos == 'Exit':
            break

    janela2.close()

def pesquisa():
    import os
    # Removendo acentos e  caracteres especiais
    if not os.path.exists(file_path):
        sg.popup("Alunos não cadastrados!!!", "Favor cadastrar os alunos para continuar.")
    else:
        if not os.path.exists(file_path2):
            sg.popup("Lista não cadastrada!!!", "Favor cadastrar a lista para continuar.")
        else:
        # Do something with the file
            import unicodedata
            import os
            def remove_accents(input_str):
                nfkd_form = unicodedata.normalize('NFD', input_str)
                return "".join([c for c in nfkd_form if not unicodedata.combining(c)])
            for file in os.listdir("/"):
                with open("alunos.txt", "r") as f:
                    file_contents = f.read()
            
                file_contents = remove_accents(file_contents)
    
                with open("alunos.txt", "w") as f:
                    f.write(file_contents)
            
                with open("lista.txt", "r") as f:
                    file_contents = f.read()
            
                file_contents = remove_accents(file_contents)
            
                with open("lista.txt", "w") as f:
                    f.write(file_contents)
                    
                # Deixando a primeira letra do nome em maiúscula
            
                with open("alunos.txt", "r") as f:
                    lines = f.readlines()
            
                lines = [line.title() for line in lines]
            
                with open("alunos.txt", "w") as f:
                    f.writelines(lines)
            
                with open("lista.txt", "r") as f:
                    lines = f.readlines()
            
                lines = [line.title() for line in lines]
            
                with open("lista.txt", "w") as f:
                    f.writelines(lines)
                
                # Comparando nomes entre as listas
                
                with open("alunos.txt", 'r') as l1, open("lista.txt", 'r') as l2:
                    lines1 = l1.readlines()
                    lines2 = l2.readlines()
                    common_lines = []
                    for linha in lines1:
                        campo = linha.replace("\n", "").split(";")
                        for linha1 in lines2:
                            campo1 = linha1.replace("\n", "").split(";")
                            if campo[0] == campo1[0]:
                                common_lines.append("Nome: "+ campo[0] + " Turma: " + campo[1] + " Curso: "+ campo1[1])
                    with open("resultado.txt", "w") as f:
                        f.write("\n".join(common_lines))
            
    with open("resultado.txt", "r") as f:
        file_exibir = f.read()

        layout3 = [
            [sg.Text('Alunos Aprovados')],
            [sg.Multiline(file_exibir ,size=(WIN_W, WIN_H))],
            [sg.Button('Sair')]
        ]
        janela3 = sg.Window(version, layout3)

        while True:
            event = janela3.read()
            if event in (None, 'Sair'):
                janela3.close()
                break   
                   
            
def Exibir():
    import os
    if not os.path.exists(file_path):
        sg.popup("Alunos não cadastrados!!!", "Favor cadastrar os alunos para continuar.")
    else:
        with open("alunos.txt", "r") as f:
            file_exibir = f.read()

    layout4 = [
        [sg.Text('Alunos Cadastrados')],
        [sg.Multiline(file_exibir ,size=(WIN_W, WIN_H))],
        [sg.Button('Sair', key= 'Sair')]
    ]
    janela4 = sg.Window(version, layout4)
    while True:
        event = janela4.read()
        if event in (None, 'Sair'):
            janela4.close()
            break
            

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Exit':
        break
    if eventos in ("Alunos"):
        Exibir()
    if eventos in (cadastro, "n:78"):
        alunos()
    if eventos in (lista, "o:79"):
        listas()
    if eventos in (pesquisar, "s:83"):
        pesquisa()
    if eventos in ("Sobre"):
        [sg.popup(sobre)]

window.close()
