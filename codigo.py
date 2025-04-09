import pyautogui

pyautogui.PAUSE = 0.5 # adicionando um dalay entre as tarefas

# abrir o Safari no Mac
pyautogui.hotkey('command','space')
pyautogui.write('safari')
pyautogui.press('enter')

# entrar no site da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')