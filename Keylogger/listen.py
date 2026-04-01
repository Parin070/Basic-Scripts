from pynput.mouse import Listener

def writetofile(x,y):
    print(f"Current position of mouse {x},{y}")

with Listener(on_move=writetofile)as l:
    l.join()