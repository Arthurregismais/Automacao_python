import pyautogui
import time

if __name__ == '__main__':
    pyautogui.alert('Por favor, não mexa no teclado ou no mouse durante a execução do código')
    pyautogui.PAUSE = 0.75
#Abrir o google drive no meu computador

    pyautogui.press('winleft')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
    pyautogui.press('enter')

#Entrar na àrea de trabalho
    pyautogui.hotkey('winleft', 'd')
    pyautogui.moveTo(180, 443)
    pyautogui.mouseDown()
    pyautogui.moveTo(757, 582)

#Enquanto arrasto, mudo para o google drive
    pyautogui.hotkey('alt', 'tab')

#largando o arquivo no drive
    pyautogui.mouseUp()

#Esperar 5 segundos
    time.sleep(5)
    pyautogui.alert('O código acabou de rodar, pode usar seu computador novamente ')


