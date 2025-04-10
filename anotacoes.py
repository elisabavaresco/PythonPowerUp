""""
Antes de começar qualquer projeto, é importante entender qual seria o passo a passo manual que seria executado, qual a lógica que ele deve execuitar, para depois traduzir isso para código. 
Este é um projeto de automação de tarefas, mais especificamente, automação de cadastro de produtos.

Lógica:
Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
    Abrir o Chrome
    Digitar o site
Passo 2: Fazer login
    Clicar no campo de email
    Escrever o email
    Clicar no campo de senha
    Escrever a senha
    Clicar no botão de login
Passo 3: Importar a base de dados
Passo 4: Cadastrar 1 produto
Passo 5: Repetir para todos os produtos

Bibliotecas:
pyautogui -> uma das bibliotecas que vamos utilizar nesse projeto é a 'pyautogui', que faz automações com Python, permitindo que você controle o teclado, mause e tela usando Python
    pyautogui.click -> clicar em algum lugar
    pyautogui.press -> apertar 1 tecla
    pyautogui.write -> escrever um texto
    pyautogui.hotkey -> apertar uma combinação de teclas
    pyautogui.PAUSE -> para dar um daley entre as tarefas
time -> biblioteca para controle de tempo do código
pandas -> pacote para nos ajudar a importar base de dados (seja base de dados em csv, excel, html, json, sas, etc)
"""