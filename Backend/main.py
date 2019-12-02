from spellchecker import SpellChecker
from pynput.keyboard import Key, Listener
import logging
from pyautogui import typewrite, hotkey

spell = SpellChecker('en')


Elissa_dict = './dictionary.txt'
spell.word_frequency.load_text_file(Elissa_dict, 'utf-8')


dirty = open('./bad_words.txt', 'r', encoding='utf-8-sig')
junk = dirty.read().splitlines()
dirty.close()
spell.word_frequency.remove_words(junk)


def autocorrect():
    current_string = open('./keyLog.txt', 'r+', encoding='utf-8-sig')
    string = current_string.read()
    current_string.truncate(0)
    correct = spell.correction(string)
    if len(string) != 0 and string != correct:
        return correct


log_dir = "/Users/GerudoValley/Desktop/Ratz4Lyfe/"
logging.basicConfig(filename=(log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s')


keys = []
shifted = False


def in_alphabet(key):
    return 32 < ord(key) < 127


def on_release(key):
    global keys, shifted, corrected
    try:
        if key == Key.space:
            write_file(keys)
            corrected = autocorrect()
            if not corrected:
                keys = []
                return
            press('backspace')
            hotkey('ctrl', 'backspace')
            typewrite(corrected)
            keys = []
            return
        elif key == Key.backspace:
            keys.pop()
            return
        elif key == Key.shift:
            shifted = True
            return


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