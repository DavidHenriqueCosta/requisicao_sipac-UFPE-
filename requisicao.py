import pyautogui
import time
import tkinter as tk
from getpass import getpass


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
gpmaterial = 0
grupomaterial = gpmaterial
usuario = str
senha = getpass


def get_input():
    global gpmaterial
    global finalidade
    global usuario
    global senha
    gpmaterial = gp.get()

    usuario = user.get()
    senha = senha.get()
    window.destroy() 

window = tk.Tk()
label = tk.Label(window, text='Qual o grupo material da requisição que será cadastrada?')
label.pack()
gp = tk.Entry(window)
gp.pack()
grupomaterial == tk.Entry(window)
label = tk.Label (window, text='O Grupo material possui finalidade ? qual seria : ')
label.pack()
fnd = tk.Entry(window)
fnd.pack()

label = tk.Label(window, text='Qual é o seu login ?') 
label.pack()
user = tk.Entry(window)
user.pack()
usuario == tk.Entry(window)
label = tk.Label(window, text='Qual a sua senha ?')
label.pack()
senha = tk.Entry(window, show="*")
senha.pack()
senha == tk.Entry(window)
button = tk.Button(window, text='Confirmar', command=get_input)
button.pack()
window.mainloop()

pyautogui.hotkey("win","r")
pyautogui.typewrite("https://sipac.ufpe.br/public/jsp/portal.jsf \n")
time.sleep(10)

pyautogui.click(pyautogui.locateCenterOnScreen("img\\login.png", confidence=0.8), duration=0.5)
time.sleep(10)
pyautogui.typewrite(usuario, interval=0.08)
time.sleep(1.5)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\senha.png", confidence=0.8), duration=0.5)
pyautogui.typewrite(senha, interval=0.08)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\entrar.png", confidence=0.8), duration=0.5)
time.sleep(10)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\usuario_do_sistema.png", confidence=0.8), duration=0.5)
time.sleep(2)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\trocar_usuario.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\1100.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\alterar.png", confidence=0.8), duration=0.5)
time.sleep(10)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("img\\requisicoes.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("img\\material_servico.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("img\\mover_antes_do_cadastrar1.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("img\\compra.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.moveTo(pyautogui.locateCenterOnScreen("img\\mover_antes_do_cadastrar2.png", confidence=0.8), duration=0.5)
time.sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\cadastrar_requisicao.png", confidence=0.8), duration=0.5)
time.sleep(5)
pyautogui.click(pyautogui.locateCenterOnScreen("img\\nacional_nrp.png", confidence=0.8), duration=0.5)
time.sleep(8)

pyautogui.typewrite(gpmaterial)
time.sleep(3)
pyautogui.hotkey('tab')
pyautogui.click(pyautogui.locateCenterOnScreen("img\\continuar.png", confidence=0.8), duration=0.5)
time.sleep(5)



with open("planilha.csv") as f:
    next(f)

    for line in f:
        line=line.strip()
        line=line.split(";")
        print("Dados: ",line)

        codigosipac = line[0]
        valor = line[1]
        quantidade = line[2]
        pyautogui.press('f5')
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\codigo_do_material.png", confidence=0.8), duration=0.1)
        pyautogui.typewrite(codigosipac, interval=0.05)
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\buscar_material.png", confidence=0.8), duration=0.1)
        time.sleep(3)
       # pyautogui.press('f5')
        #time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\seta_verde.png", confidence=0.8), duration=0.1)
       # time.sleep(3)
        #pyautogui.press('f5')
        time.sleep(3)
        pyautogui.press('enter')
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\valor_estimado.png", confidence=0.8), duration=0.1)
        time.sleep(3)
        i = 0
        while i<6:
            pyautogui.press('right')
            i = i+1
        l = 0
        while l<6:
            pyautogui.press('backspace')
            l = l+1
       
        pyautogui.typewrite(valor, interval=0.05)
        time.sleep(4)
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\quantidades.png", confidence=0.8), duration=0.1)
        time.sleep(1)
        i = 0
        while i<6:
            pyautogui.press('right')
            i = i+1
        l = 0
        while l<6:
            pyautogui.press('backspace')
            l = l+1

        pyautogui.typewrite(quantidade, interval=0.05)
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen("img\\incluir.png", confidence=0.8), duration=1)
        time.sleep(5)

#pyautogui.screenshot(imageFilename='novarequisicao')
pyautogui.screenshot(f"requisicoes_cadastradas\\REQUISIÇÃO{gpmaterial}.png")
pyautogui.alert(text="programa finalizado com sucesso",title="aviso do sistema",button=100)