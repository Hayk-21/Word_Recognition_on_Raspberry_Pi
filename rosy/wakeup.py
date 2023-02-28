import sounddevice as sd
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
import tensorflow as tf
# Հայտարարեցինք անհրաժեշտ գրադարանները


lcd = Adafruit_CharLCD(rs=22, en=23, d4=24, d5=25, d6=26, d7=27, cols=16, lines=2)
# Այստեղ տալիս ենք մեր էկրանի "Port"-էրը, դրանք raspberry pi-ին միացվող լարերն են

lcd.message('Loading Model...') 
imported = tf.saved_model.load("saved_2") # Tensorflow-ի մեթդը օգտագործելով վերցնում ենք մեր ուսուցանած մոդելը
samplerate = 16000 # Սա մեր ձայնի հաճախությունն է, վերցնում ենք ստանդարտ 16,000 հերց
lcd.message('Start!')


def func():
    recognize = False

    while True: # անվերջ loop
        lcd.clear() # մաքրում ենք էկրանը
        lcd.message('*_*') # տպում ենք էկրանին *_*
        
        # ձայնագրենք մեր ձայնը 16 000 հերց հաճախությամբ
        recording = sd.rec(int(1*samplerate),samplerate = samplerate , channels = 1, dtype='float32').ravel() 
        sd.wait() # սպասում է ձայնագրության ավարտին
        lcd.clear() 
        # փոփոխենք մեր ձայնային տվյալները դերձնելով մեզ հարմար
        recording = recording[tf.newaxis, :]
        # հաջորթիվ մոդելը ճանաչում է ձայնը
        pred = imported(recording)['class_names'][0].numpy()
        pred = pred.decode('utf-8')

        if recognize == False and pred == 'marvin': # եթե հնչել է marvel բառը, սարքը սկսում է իր աշխատանքը
            lcd.message("Hello\nI'm listening!")
            recognize = True
            sleep(5)
        elif recognize == True and pred == 'stop': # սարքը ավարտում է աշխատանքը
            recognize = False
            lcd.message('OK !')
            sleep(1)
        elif recognize == True and pred != 'noise': # ուղակի աղմուկի դեպքում սարքը ոչինչ չի տպում էկրանին
            lcd.message('-_-\n'+pred)
            sleep(2)
        #lcd.message(pred)
        #sleep(2)
        lcd.clear()
        lcd.message('-_-')
        sleep(0.1) # 0․1վ սպասում է սարքը որպիսի loop-ը ձայնագրության հետ խնդիրներ չունենա


if __name__ == '__main__':
    func() # աշխատացնում ենք մեր հիմնական ֆունկցիան


