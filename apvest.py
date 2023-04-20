import os
import PySimpleGUI as sg

sobre ='''
ApVest

Version: 2.5.0
Date: 2023-02-21

Criado por:
Jamisson Luis & Mário André
'''
# Layout
sg.theme('SystemDafault')

WIN_W: int = 90
WIN_H: int = 25

# Variáveis ​​de string para reduzir o loop e o código do menu!
cadastro: str = "+ Aluno"
lista: str = "+ Lista"
pesquisar: str = "Pesquisar"
exibir: str = "Alunos"
version = "ApVest Version 2.5.0"

#busca
file_path = "alunos.txt"
file_path2 = "lista.txt"

# Menu
menu_layout: list = [
    ["Exibir", ["Alunos","Lista"]],
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
                break
        elif eventos == sg.WIN_CLOSED or eventos == 'Exit':
            break

    janela1.close()
def listas(): 
    layout2 = [
        [sg.Text('Insira os nomes da lista dos aprovados.')],
        [sg.Multiline(size=(WIN_W, WIN_H), key="_lista_")],
        [sg.Button('Salvar'),sg.Button('Exit'), sg.Button('Importar PDF')],
    ]

    janela2 = sg.Window('version', layout2)
    
    while True:
        eventos, valores = janela2.read()
        if eventos == 'Salvar':
            with open("lista.txt", "w") as f:
                f.write(valores['_lista_'])
                break
        elif eventos == 'Importar PDF':
            importar()
            break
        elif eventos == sg.WIN_CLOSED or eventos == 'Exit':
            break

    janela2.close()
def pesquisa():
    # Removendo acentos e  caracteres especiais
    if not os.path.exists(file_path):
        sg.popup("Alunos não cadastrados!!!", "Favor cadastrar os alunos para continuar.")
    else:
        if not os.path.exists(file_path2):
            sg.popup("Lista não cadastrada!!!", "Favor cadastrar a lista para continuar.")
        else:
        # Do something with the file
            import unicodedata

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
                
                    with open('alunos.txt', 'r') as arquivo:
                        linhas = arquivo.readlines()

                    for i in range(len(linhas)):
                        linhas[i] = linhas[i].rstrip()
                        while linhas[i] and linhas[i][-1].isdigit():
                            linhas[i] = linhas[i][:-1].rstrip()

                    with open('alunoa.txt', 'w') as arquivo:
                        for linha in linhas:
                            arquivo.write(linha + '\n')

                    with open("lista.txt", "r") as f:
                        lines = f.readlines()
                
                    lines = [line.title() for line in lines]
                
                    with open("lista.txt", "w") as f:
                        f.writelines(lines)
                
                    with open('lista.txt', 'r') as arquivo:
                        linhas = arquivo.readlines()

                    for i in range(len(linhas)):
                        linhas[i] = linhas[i].rstrip()
                        while linhas[i] and linhas[i][-1].isdigit():
                            linhas[i] = linhas[i][:-1].rstrip()

                    with open('lista.txt', 'w') as arquivo:
                        for linha in linhas:
                            arquivo.write(linha + '\n')

                    # Comparando nomes entre as listas
                
                    with open("lista.txt") as f1, open("alunos.txt") as f2:
                        file1_lines = set(f1.read().splitlines())
                        file2_lines = set(f2.read().splitlines())
                        common_lines = file1_lines & file2_lines
                
                    with open("resultado.txt", "w") as f3:
                        for line in common_lines:
                            f3.write(line + "\n")
                
                    with open("resultado.txt", "r") as f4:
                            result = f4.read()

                    #sg.popup(result)
                    os.system ("resultado.txt")
        
                    break
def Exibir():
    if not os.path.exists(file_path):
        sg.popup("Alunos não cadastrados!!!", "Favor cadastrar os alunos para continuar.")
    else:
        with open("alunos.txt", "r") as f:
            file_exibir = f.read()

            layout3 = [
               [sg.Text('Alunos Cadastrados')],
               [sg.Multiline(file_exibir ,size=(WIN_W, WIN_H))],
               [sg.Button('Exit')]
            ]
            janela3 = sg.Window(version, layout3)

        while True:
            eventos, valores = janela3.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Exit':
                break

        janela3.close()
def Exibir2():
    if not os.path.exists(file_path2):
        sg.popup("Lista não cadastrada!!!", "Favor adcionar lista para continuar.")
    else:
        with open("lista.txt", "r") as f:
            file_exibir = f.read()

            layout5 = [
               [sg.Text('Lista Cadastrada')],
               [sg.Multiline(file_exibir ,size=(WIN_W, WIN_H))],
               [sg.Button('Exit')]
            ]
            janela5 = sg.Window(version, layout5)

        while True:
            eventos, valores = janela5.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Exit':
                break

        janela5.close()
def importar():
        layout4 = [
            [sg.Text("Procure o PDF:")],
            [sg.InputText(key="-FILE_PATH-"), sg.FileBrowse(initial_folder='', file_types=[("Arquivo PDF", "*.pdf")])],
            [sg.Button('Importar'), sg.Exit()]
            ]

        janela4 = sg.Window('Teste', layout4)
        while True:
            eventos, valores = janela4.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Exit':
                break
            #elif eventos == 'Importar':

                with open((valores['-FILE_PATH-']), "rb") as pdf_file:
                    reader = PdfReader(pdf_file)
                    numpages = (len(reader.pages))
                    contador = 0
                    while (contador < numpages):
                        pageobj=reader.pages[contador]
                        contador   = contador + 1
                        text=pageobj.extract_text()
                        file1=open("lista.txt","a")
                        file1.writelines(text)
                #break
        janela4.close()

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Exit':
        break
    if eventos in ("Alunos"):
        Exibir()
    if eventos in ("Lista"):
        Exibir2()
    if eventos in (cadastro, "n:78"):
        alunos()
    if eventos in (lista, "o:79"):
        listas()
    if eventos in (pesquisar, "s:83"):
        pesquisa()
    if eventos in ("Sobre"):
        [sg.popup(sobre)]

window.close()
