from pynput.keyboard import Key, Listener
import logging

from pyautogui import typewrite, hotkey

log_dir = r"C:/users/Cameron/Desktop/1P03/LawtoCorrect/backend/"
logging.basicConfig(filename=(log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s')

keys = []
shifted = False
corrected


def in_alphabet(key):
    return 32 < ord(key) < 127


def on_release(key):
    global keys, shifted, corrected
    try:
        if key == Key.space:
            write_file(keys)
            #corrected = autocorrect()
            corrected = ''
            if not corrected:
                corrected = keys
            hotkey('ctrl', 'del')
            typewrite(corrected)
            keys = []
            return
        elif key == Key.backspace:
            keys.pop()
            return
        elif key == Key.shift:
            shifted = True
            return

        # print(str(key).replace("'", ""))
        if shifted and in_alphabet(str(key).replace("'", "")):
            keys.append(str(key).upper())
            shifted = False
        elif shifted and not in_alphabet(str(key).replace("'", "")):
            shifted = False
        elif in_alphabet(str(key).replace("'", "")):
            keys.append(str(key))
    except:
        pass


def write_file(keys):
    with open("keyLog.txt", "a") as f:
        f.write(" ")
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)


with Listener(on_release=on_release) as listener:
    listener.join()
