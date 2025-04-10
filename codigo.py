import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # adicionando um dalay entre as tarefas

# Passo 1: Entrar no sistema da empresa
# abrir o Safari no Mac
# pyautogui.hotkey('command','space')
# posição da lupa na tela: x=3884, y=14
pyautogui.click(3884, 14)
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

# Passo 4/5: Cadastrar produtos
for linha in tabela.index:
    # posição do primeiro campo do formulário de cadastro: x=1992, y=305
    pyautogui.click(1992, 305)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria']) # para formatar o número da tabela em string
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)
    
    # pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000) # para voltar ao topo da página