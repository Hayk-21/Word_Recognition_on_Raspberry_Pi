import sounddevice as sd
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
import tensorflow as tf

lcd = Adafruit_CharLCD(rs=22, en=23, d4=24, d5=25, d6=26, d7=27, cols=16, lines=2)

lcd.message('Loading Model...')
imported = tf.saved_model.load("saved_2")
samplerate = 16000
lcd.message('Start!')


def func():
    recognize = False

    while True:
        lcd.clear()
        lcd.message('*_*')
        #sleep(0.01)
        recording = sd.rec(int(1*samplerate),samplerate = samplerate , channels = 1, dtype='float32').ravel()
        sd.wait()
        lcd.clear()
        recording = recording[tf.newaxis, :]
        pred = imported(recording)['class_names'][0].numpy()
        pred = pred.decode('utf-8')

        if recognize == False and pred == 'marvin':
            lcd.message("Hello\nI'm listening!")
            recognize = True
            sleep(5)
        elif recognize == True and pred == 'stop': 
            recognize = False
            lcd.message('OK !')
            sleep(1)
        elif recognize == True and pred != 'noise':
            lcd.message('-_-\n'+pred)
            sleep(2)
        #lcd.message(pred)
        #sleep(2)
        lcd.clear()
        lcd.message('-_-')
        sleep(0.1)


if __name__ == '__main__':
    func()


