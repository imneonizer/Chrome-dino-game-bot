import pyautogui
import time
import PIL.ImageGrab as ImageGrab
pyautogui.FAILSAFE = True

box_area1 = (248, 206, 286, 250) #box coordinates(x1,y1, x2,y2) to detect obstacles
pixel_plant1 = (19, 9) #pixel coordinates(x1,y1) to detect plants
pixel_plant2 = (11, 21) #pixel coordinates(x1,y1) to detect plants
pixel_plant3 = (29, 15) #pixel coordinates(x1,y1) to detect plants
pixel_plant4 = (20, 33) #pixel coordinates(x1,y1) to detect plants
pixel_plant5 = (20, 42) #pixel coordinates(x1,y1) to detect plants

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    print('Jump')
play = True
while play:
    try:
        box = ImageGrab.grab(box_area1)
        p1 = box.getpixel(pixel_plant1)
        p2 = box.getpixel(pixel_plant2)
        p3 = box.getpixel(pixel_plant3)
        p4 = box.getpixel(pixel_plant4)
        p5 = box.getpixel(pixel_plant5)
        if p1 == (83, 83, 83) or p2 == (83, 83, 83) or p3 == (83, 83, 83) or p4 == (83, 83, 83) or p5 == (83, 83, 83):
            jump()
            time.sleep(0.06)
    except Exception as e:
        play = False
        print(e)
