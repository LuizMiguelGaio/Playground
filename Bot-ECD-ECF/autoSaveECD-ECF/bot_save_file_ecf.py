import pyautogui

#criado com intuito de salvar os arquivos de ECF.
#executar bot depois de assinar a ECF

pyautogui.PAUSE = 2
#area de trabalho
pyautogui.moveTo(1433, 876)
pyautogui.doubleClick()
#clicar no programa
pyautogui.moveTo(282, 872)
pyautogui.doubleClick()
#duploclick pra abrir o recibo
pyautogui.moveTo(962, 360) #TRANSMITA<Duplo click para RECIBO>
pyautogui.doubleClick()
pyautogui.moveTo(676, 465) #"Sim"
pyautogui.leftClick()
pyautogui.PAUSE = 5
#salvar recibo de transmissão
pyautogui.PAUSE = 2
pyautogui.moveTo(245, 109)#salvar
pyautogui.leftClick()
pyautogui.moveTo(503, 349)#pasta
pyautogui.doubleClick()
pyautogui.moveTo(245, 109)#click_preencher_nome
pyautogui.leftClick()
pyautogui.write("Recibo de entrega de Escrituração fiscal")
pyautogui.moveTo(874, 586)#click_gravar
pyautogui.leftClick()
#fechar janela recibo
pyautogui.moveTo(1194, 83)#click_fechar
pyautogui.leftClick()
pyautogui.moveTo(770, 629)#click_fechar2
pyautogui.leftClick()
#relatorio>impressao de pastas e fichas>marcar boxs> visualisar> 180seg pra abrir
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
pyautogui.moveTo(666, 214) #Relatório de impressao de pastas
pyautogui.leftClick()
pyautogui.moveTo(617, 153) #checkbox 1
pyautogui.leftClick()
pyautogui.moveTo(811, 153) #checkbox 2
pyautogui.leftClick()
pyautogui.moveTo(1319, 153) #checkbox 3
pyautogui.leftClick()
pyautogui.moveTo(1378, 153) #checkbox 4
pyautogui.leftClick()
pyautogui.moveTo(923, 746) #Visualizar
pyautogui.leftClick()
pyautogui.PAUSE = 180

#salvando relatorio de pastas e fichas> clicar home>biblioteca> documentos> 40seg pra salvar>clicar no OK
pyautogui.moveTo(424, 229) #botão salvar
pyautogui.PAUSE = 2
pyautogui.leftClick()
pyautogui.moveTo(876, 301) #home
pyautogui.leftClick()
pyautogui.moveTo(531, 336) #biblioteca
pyautogui.doubleClick()
pyautogui.moveTo(531, 336) #documentos
pyautogui.doubleClick()
pyautogui.moveTo(785, 528) #Escrever o nome do documento
pyautogui.leftClick()
pyautogui.write("Relatorio de impressao de pastas e fichas")
pyautogui.moveTo(724, 366) #clique na pasta
pyautogui.doubleClick()
pyautogui.moveTo(1079, 606) #Grava
pyautogui.leftClick()

#relatorio>balanco patrimonial>periodo: todos>visualizar>5seg>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
pyautogui.moveTo(693, 233) #Balanço Patrimonial
pyautogui.leftClick()
pyautogui.moveTo(911, 165) #seleciona o periodo
pyautogui.leftClick()
pyautogui.moveTo(845, 254) #todos
pyautogui.leftClick()
pyautogui.moveTo(925, 225) #visualizar
pyautogui.leftClick()
pyautogui.PAUSE = 3
pyautogui.moveTo(431, 167) #botão salvar
pyautogui.leftClick()
pyautogui.PAUSE = 2
pyautogui.write("Balanço Patrimonial")
pyautogui.moveTo(723, 365) #clique na pasta
pyautogui.doubleClick()
pyautogui.moveTo(1079, 606) #Grava
pyautogui.leftClick()

#relatorio>DRE > contas contaveis> > visualizar>3seg>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
pyautogui.moveTo(635, 253) #DRE
pyautogui.leftClick()
pyautogui.moveTo(635, 253) #DRE - Contas Contábeis
pyautogui.leftClick()
pyautogui.moveTo(911, 165) #seleciona o periodo
pyautogui.leftClick()
pyautogui.moveTo(845, 254) #todos
pyautogui.leftClick()
pyautogui.moveTo(925, 225) #visualizar
pyautogui.leftClick()
pyautogui.PAUSE = 3
pyautogui.moveTo(431, 167) #botão salvar
pyautogui.leftClick()
pyautogui.PAUSE = 2
pyautogui.write("DRE")
pyautogui.moveTo(723, 365) #clique na pasta
pyautogui.doubleClick()
pyautogui.moveTo(1079, 606) #Grava
pyautogui.leftClick()

#relatorio>LALUR>LALUR parte A>periodo:todos>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
pyautogui.moveTo(642, 273) #LALUR
pyautogui.leftClick()
pyautogui.moveTo(914, 269) #LALUR parte A
pyautogui.leftClick()
pyautogui.moveTo(772, 164) #primeiro semestre v2
pyautogui.leftClick()
pyautogui.moveTo(720, 251) #todos v2
pyautogui.leftClick()
pyautogui.moveTo(1209, 166) #visualizar v2
pyautogui.leftClick()
pyautogui.PAUSE = 3
pyautogui.moveTo(431, 167) #botão salvar
pyautogui.leftClick()
pyautogui.PAUSE = 2
pyautogui.write("LALUR - A")
pyautogui.moveTo(723, 365) #clique na pasta
pyautogui.doubleClick()
pyautogui.moveTo(1079, 606) #Grava
pyautogui.leftClick()

#relatorio>LALUR>LALUR parte B>periodo:todos>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
pyautogui.moveTo(642, 273) #LALUR
pyautogui.leftClick()
pyautogui.moveTo(929, 289) #LALUR parte B
pyautogui.leftClick()
pyautogui.moveTo(772, 164) #primeiro semestre v2
pyautogui.leftClick()
pyautogui.moveTo(720, 251) #todos v2
pyautogui.leftClick()
pyautogui.moveTo(1209, 166) #visualizar v2
pyautogui.leftClick()
pyautogui.PAUSE = 3
pyautogui.moveTo(431, 167) #botão salvar
pyautogui.leftClick()
pyautogui.PAUSE = 2
pyautogui.write("LALUR - B")
pyautogui.moveTo(723, 365) #clique na pasta
pyautogui.doubleClick()
pyautogui.moveTo(1079, 606) #Grava
pyautogui.leftClick()
#relatorio>LALUR>LACS parte A>periodo:todos>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()
#relatorio>LALUR>LACS parte B>periodo:todos>salva
pyautogui.moveTo(628, 123) #Relatório
pyautogui.leftClick()


