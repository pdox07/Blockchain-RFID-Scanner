import RPi.GPIO as GPIO
import time
  
def setup(pin):
    BuzzerPin = pin
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
 
def on(BuzzerPin):
    GPIO.output(BuzzerPin, GPIO.LOW)
 
def off(BuzzerPin):
    GPIO.output(BuzzerPin, GPIO.HIGH)
 
def beep(x, BuzzerPin):
    on(BuzzerPin)
    time.sleep(x)
    off(BuzzerPin)
    time.sleep(x)
 
def loop(BuzzerPin):
    while True:
        beep(0.5, BuzzerPin)
        
def destroy(BuzzerPin):
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup() 

if __name__ == '__main__': 
    setup(BuzzPin)
    try:
        loop(BuzzerPin)
    except KeyboardInterrupt:
        destroy()