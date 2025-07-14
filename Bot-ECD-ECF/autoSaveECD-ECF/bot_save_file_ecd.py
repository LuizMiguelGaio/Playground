import pyautogui
import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    messagebox.showinfo("Sucesso", "Arquivos salvos com sucesso.")

pyautogui.FAILSAFE = True

#pyautogui.PAUSE = 2.5
#pyautogui.moveTo(, ) # mover para
#pyautogui.click()  # click the mouse
#pyautogui.doubleClick()  # perform a left-button double click
#pyautogui.write('', interval=0.25) #escreve oque esta escrito
#pyautogui.press('enter')  # press the Enter key

pyautogui.PAUSE = 2.0 #tempo entre acoes

pyautogui.moveTo(274, 881) #abrir programa
pyautogui.click()  # click the mouse

#salvar recido de transmissão
pyautogui.moveTo(393, 127) #escrituracao
pyautogui.click()  # click the mouse

pyautogui.moveTo(383,314 ) # recibo de transmissao
pyautogui.click()  # click the mouse

pyautogui.moveTo(349,167 ) # botao salvar
pyautogui.click()  # click the mouse

pyautogui.write('Recibo de entrega de Escrituração fiscal', interval=0.25) #escreve

pyautogui.moveTo(675,354 ) # mover para pasta
pyautogui.click()  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('enter')  # press the Enter key

#salvar diario
pyautogui.moveTo(393, 127) #escrituracao
pyautogui.click()  # click the mouse

pyautogui.moveTo(396,354 ) # visualizacoes
pyautogui.click()  # click the mouse
pyautogui.moveTo(621,386 ) # diario
pyautogui.click()  # click the mouse


pyautogui.moveTo(1384,243 ) # visualizar
pyautogui.click()  # click the mouse

pyautogui.PAUSE = 7.0

pyautogui.moveTo(349,167 ) # botao salvar
pyautogui.PAUSE = 2.0
pyautogui.click()  # click the mouse

pyautogui.write('Diario', interval=0.25) #escreve

pyautogui.moveTo(675,354 ) # mover para pasta
pyautogui.click()  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('enter')  # press the Enter key

#salvar balanco patrimonial

pyautogui.moveTo(393, 127) #escrituracao
pyautogui.click()  # click the mouse

pyautogui.moveTo(396,354 ) # visualizacoes
pyautogui.click()  # click the mouse
pyautogui.moveTo(628,447 ) # Demostracoes contabeis
pyautogui.click()  # click the mouse
pyautogui.moveTo(843,447 ) # balanco patrimonial
pyautogui.click()  # click the mouse

pyautogui.moveTo(521,210 ) # periodo
pyautogui.click()  # click the mouse

pyautogui.moveTo(865,378 ) # visualizar banlanco
pyautogui.click()  # click the mouse

pyautogui.PAUSE = 7.0

pyautogui.moveTo(349,167 ) # botao salvar
pyautogui.PAUSE = 2.0
pyautogui.click()  # click the mouse

pyautogui.write('Balanço Patrimonial', interval=0.25) #escreve

pyautogui.moveTo(675,354 ) # mover para pasta
pyautogui.click()  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('enter')  # press the Enter key

#DRE
pyautogui.moveTo(393, 127) #escrituracao
pyautogui.click()  # click the mouse

pyautogui.moveTo(396,354 ) # visualizacoes
pyautogui.click()  # click the mouse
pyautogui.moveTo(628,447 ) # Demostracoes contabeis
pyautogui.click()  # click the mouse
pyautogui.moveTo(843,468 ) # balanco patrimonial
pyautogui.click()  # click the mouse

pyautogui.moveTo(521,210 ) # periodo
pyautogui.click()  # click the mouse

pyautogui.moveTo(865,378 ) # visualizar banlanco
pyautogui.click()  # click the mouse

pyautogui.PAUSE = 7.0

pyautogui.moveTo(349,167 ) # botao salvar
pyautogui.PAUSE = 1.5
pyautogui.click()  # click the mouse

pyautogui.write('DRE', interval=0.25) #escreve

pyautogui.moveTo(675,354 ) # mover para pasta
pyautogui.click()  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('enter')  # press the Enter key

#Salvar Termo de abertura e encerramento

pyautogui.moveTo(393, 127) #escrituracao
pyautogui.click()  # click the mouse

pyautogui.moveTo(396,354 ) # visualizacoes
pyautogui.click()  # click the mouse
pyautogui.moveTo(620,589 ) # Termo de abertura e encerramento
pyautogui.click()  # click the mouse

pyautogui.PAUSE = 7.0

pyautogui.moveTo(349,167 ) # botao salvar
pyautogui.PAUSE = 1.5
pyautogui.click()  # click the mouse

pyautogui.write('Termo de Abertura e encerramento', interval=0.25) #escreve

pyautogui.moveTo(675,354 ) # mover para pasta
pyautogui.click()  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('enter')  # press the Enter key

exibir_mensagem()

#pyautogui.moveTo(, ) # mover para
#pyautogui.click()  # click the mouse