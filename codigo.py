import pyautogui

# abrir o Safari no Mac
pyautogui.hotkey('command','space')
pyautogui.write('safari')
pyautogui.press('enter')

# entrar no sistema da empresa
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')