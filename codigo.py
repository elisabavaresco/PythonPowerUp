import pyautogui
import time

pyautogui.PAUSE = 0.5 # adicionando um dalay entre as tarefas

# Passo 1: Entrar no sistema da empresa
# abrir o Safari no Mac
pyautogui.hotkey('command','space')
pyautogui.write('safari')
pyautogui.press('enter')

# entrar no site da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# esperar 3 segundos 
time.sleep(3)

# Passo 2: Fazer login
# clicar no campo de email
# posição do compo de email na tela: x=2004, y=425
pyautogui.click(2004, 425)
pyautogui.write('exemplo@gmail.com')