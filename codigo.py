import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # adicionando um dalay entre as tarefas

# Passo 1: Entrar no sistema da empresa
# abrir o Safari no Mac
pyautogui.hotkey('command','space')
# posição da lupa na tela: x=3884, y=14
# pyautogui.click(3884, 14)
time.sleep(2)
pyautogui.write('safari')
pyautogui.press('enter')

# entrar no site da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# esperar 3 segundos 
time.sleep(3)

# Passo 2: Fazer login
# clicar no campo de email
# posição do campo de email na tela: x=2004, y=425
pyautogui.click(2004, 425)
# digitar no campo de email
pyautogui.write('exemplo@gmail.com')

# clicar no campo de senha
# posição do campo de senha na tela: x=1993, y=519
# pyautogui.click(1993, 519)
pyautogui.press('tab')
# digitar no campo de senha
pyautogui.write('exemplosenha')
pyautogui.press('enter') # para 'clilcar' no botão logar

# esperar 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv('produtos.csv') # se o arquivo estiver em outro local, é preciso passar o 'endereço completo'

# Passo 4: Cadastrar 1 produto safari











