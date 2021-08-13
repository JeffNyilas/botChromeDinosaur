import pyautogui
from PIL import ImageGrab

aux = 0

while True:

	tela = ImageGrab.grab()

	for x in range(300+int(aux), 400+int(aux)):

		area = tela.getpixel((x, 460))

		if area[0] == 172:
			pyautogui.press("up")
			break

	aux += 0.0001