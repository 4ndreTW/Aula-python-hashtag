import pyautogui
import time
# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
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



import time
import pyautogui

time.sleep(5)
print(pyautogui.position())
# x=697, y=407 = email
# x=717, y=505 = senha
# x=932, y=573 = login
