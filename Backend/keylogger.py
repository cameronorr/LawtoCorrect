from pynput.keyboard import Key, Listener
import logging
log_dir = r"C:/users/Cameron/Desktop/1P03/LawtoCorrect/backend/"
logging.basicConfig(filename=(log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s')

keys = []
shifted = False


def in_alphabet(key):
    return 32 < ord(key) < 127


def on_press(key):
    global keys, shifted
    try:
        if key == Key.space:
            write_file(keys)
            keys = []
            return
        elif key == Key.backspace:
            keys.pop()
            return
        elif key == Key.shift:
            shifted = True
            return

        print(str(key).replace("'", ""))
        if shifted and in_alphabet(str(key).replace("'", "")):
            keys.append(key.upper())
            shifted = False
        elif shifted and not in_alphabet(str(key).replace("'", "")):
            shifted = False
        elif in_alphabet(str(key).replace("'", "")):
            keys.append(key)
    except:
        pass


def write_file(keys):
    with open("keyLog.txt", "a") as f:
        f.write(" ")
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()

