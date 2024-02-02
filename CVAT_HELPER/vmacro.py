from pynput.keyboard import Controller, Listener, Key
from tkinter import Tk, Button, font
import threading
import time

keyboard = Controller()
stop_pressing = False

def on_press(key):
    global stop_pressing
    if key == Key.space:
        stop_pressing = True
    elif key == Key.v:
        stop_pressing = False
        threading.Thread(target=press_v).start()

listener = Listener(on_press=on_press)
listener.start()

def press_v():
    global stop_pressing
    while True:
        if stop_pressing:
            break
        keyboard.press('v')
        keyboard.release('v')
        time.sleep(0.1)

def stop_pressing_v():
    global stop_pressing
    stop_pressing = True

def exit_program():
    stop_pressing_v()
    root.destroy()
    listener.stop()

root = Tk(className='cvat helper')
root.geometry("300x200")
# root.iconbitmap('myicon.ico')  # 아이콘 설정
btnFont = font.Font(size=20)
Button(root, text="V START", font=btnFont, command=lambda: threading.Thread(target=press_v).start(), padx=10, pady=10).pack(fill="both", expand=True)
Button(root, text="V STOP", font=btnFont, command=stop_pressing_v, padx=10, pady=10).pack(fill="both", expand=True)
Button(root, text="EXIT", font=btnFont, command=exit_program, padx=10, pady=10).pack(fill="both", expand=True)
root.mainloop()