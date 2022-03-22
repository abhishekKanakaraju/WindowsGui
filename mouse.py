import time
from pynput.mouse import Controller
import pyautogui
mouse=Controller()
time.sleep(1)

pyautogui.FAILSAFE = False
def gamestart():
	i=-1
	while(True):
		pyautogui.moveRel(0,100,duration=0.25)
		pyautogui.click()
		pyautogui.moveRel(100,0,duration=0.25)
		pyautogui.click()
		pyautogui.moveRel(0,-100,duration=0.25)
		pyautogui.click()
		pyautogui.moveRel(-100,0,duration=0.25)
		pyautogui.click()
		i=i+1
'''	pyautogui.moveTo(pyautogui.locateCenterOnScreen('xoo.PNG'),duration=0.25)
	pyautogui.moveRel(0,20,duration=0.25)
	pyautogui.dragRel(90,70,duration=0.25)
	time.sleep(5)
	mouse.position=(pyautogui.locateCenterOnScreen('class1.PNG'))
	pyautogui.moveRel(230,0,duration=0.25)
	time.sleep(1)
	pyautogui.dragRel(90,70,duration=0.25)
	time.sleep(2)
	pyautogui.moveRel(-230,-100,duration=0.25)
	time.sleep(1)
	pyautogui.click()
	time.sleep(2)
	pyautogui.click()'''
	
def main():
	gamestart()
	
	
	
main()	
'''
mouse.move=(300,100)
time.sleep(1)
mouse.move=(400,100)
mouse.release(Button.left)
time.sleep(1)
mouse.move=(100,100)
mouse.press(Button.left)
time.sleep(1)
mouse.move=(200,200)
time.sleep(1)
mouse.move=(300,300)
time.sleep(1)
mouse.position=(400,400)
mouse.release(Button.left)
time.sleep(1)
'''