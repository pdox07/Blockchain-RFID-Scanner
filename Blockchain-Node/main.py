import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from buzz import setup, beep, destroy
from blockchain import save_to_chain
from geo import get_geo

BuzzPin = 11 # Raspberry Pi GPIO 17
reader = SimpleMFRC522()

last_id = ""

setup(BuzzPin)
reg,lat,log = get_geo()

while True:
    try:
        id, text = reader.read()
        beep(0.5, BuzzPin)

        if id != last_id:
            data = {"id":id,
                    "text":text,
                    "reg":reg,
                    "lat":lat,
                    "log":log}
            last_id = id
            save_to_chain(data)

    finally:
        destroy(BuzzPin)