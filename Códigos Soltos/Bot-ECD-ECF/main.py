import shutil, os
import pyautogui

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)



#os.chdir('C:\\')
#shutil.copy('C:\\spam.txt', 'C:\\delicious\\cats')
#shutil.move('C:\\spam2.txt', 'C:\\delicious\\eggs.txt')
