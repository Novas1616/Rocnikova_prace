import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid

kb = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP15)
button.switch_to_input(pull=digitalio.Pull.UP)

last = True
while True:
    v = button.value 
    if last and not v:         
        kb.press(Keycode.A)   
        kb.release_all()
        time.sleep(0.2)        
    last = v
    time.sleep(0.01)
