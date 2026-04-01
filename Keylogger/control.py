from pynput.mouse import Controller as msCon
from pynput.keyboard import Controller as keyCon

def controlMouse():
    mouse = msCon()
    mouse.position = (50,100)

def controlKeyboard():
    keyboard = keyCon()
    keyboard.type("Lorem Ipsum sum sum talm pmo kgf")

controlMouse()
controlKeyboard()