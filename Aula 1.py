import pandas
import pyautogui
import time
tabela = pandas.read_csv("produtos.csv")
# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# p'yautogui.press -> aperta uma tecla
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
# pyautogui.hotkey ->  aperta um atalho (hotkey)
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=697, y=407)
pyautogui.write("andrelucastw2@gmail.com")
pyautogui.press("tab")
pyautogui.write("Lucas//@1512")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)
for linha in tabela.index:
    
    # codigo
    pyautogui.click(x=707, y=294)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    # preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    # obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    # scroll
    pyautogui.scroll(5000)

-------------------------------------------

import time
import pyautogui

time.sleep(5)
print(pyautogui.position())
# x=697, y=407 = email
# x=717, y=505 = senha
# x=932, y=573 = login
