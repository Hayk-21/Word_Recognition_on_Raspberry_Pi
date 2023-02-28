# Word Recognition on Raspberry Pi

<b>1) Download OS on Raspberry pi and make all settings.<br>
2) Download all the files needed to run our model.<br>
3) Download all the libraries that the model needs. to work.<br>
4) Connecting electrical equipment to the raspberry pi.<br>
5) Run the entire program that includes the voice recognition model.<br>
</b>

After doing all these steps you will get a similar result: <br>
Full demo: https://www.youtube.com/watch?v=gTyCxoqM1_Y <br>


https://user-images.githubusercontent.com/76138383/221869740-8f3c6774-7bec-45ea-9226-e7a13beaf514.mp4


## 1) Download OS on Raspberry pi and make all settings.
In addition to the raspberry pi, we also need a microchip above 8GB from which we will download our operating system.<br>
This video shows the process in detail.<br>
Follow the steps:<br>
https://www.youtube.com/watch?v=y45hsd2AOpw

## 2) Download all the files needed to run our model.
If you don't have the data for this issue, you can visit this GitHub link and download it.<br>
https://github.com/Hayk-21/Word_Recognition_on_Raspberry_Pi <br>
<img width="524" alt="Screenshot 2023-02-28 173232" src="https://user-images.githubusercontent.com/76138383/221869077-1ca59358-7b7a-4d42-836e-096111b286d0.png">
<br>
<b>Dataset:</b>https://drive.google.com/file/d/1Hqdolk7RXWh-nz3FdNWhGQ5GE0RD6Wwo/view?usp=share_link<br>
## 3) Download all the libraries that the model needs. to work.
All required libraries for raspberry pi are:<br>
<b>
Sound device:<br>
Adafruit_CharLCD:<br>
Tensorflow<br>
</b>
Note that raspberry os is a special type of Linux that does not work with all types of libraries. <br>
You may experience problems downloading these libraries.<br>
In that case, use google search and chatGPT to solve your problems (maybe even python version incompatibility with these libraries).<br>

## 4) Connecting electrical equipment to the raspberry pi.


<b>The screen.</b><br>
The required screen model. I2C Enabled LCD Screen<br>
It is also possible to use other LCD screens of 16x2, 4-bit mode type.<br>
You can read this tutorial to get a better idea.<br>
https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/<br>
<br>
Here are the pin connection views:<br>
![LCD-Display01](https://user-images.githubusercontent.com/76138383/221866881-80698f78-251b-4836-bc2e-5beab2ab8450.png)

Use a breadboard to make your work easier.<br>
Be careful to connect all the wires, because there is a possibility that the device will fail.

<b>Sound receiving device</b><br>
Any USB type of sound-receiving device that will connect to the raspberry pi via USB and the microphone via micro jack.<br>
![IMG_20230227_200112](https://user-images.githubusercontent.com/76138383/221867326-cfbe43fe-f4f6-4e08-8046-6d8bfdead87f.jpg)
![IMG_20230227_200044](https://user-images.githubusercontent.com/76138383/221867334-fc430a16-a0a4-4273-98e7-1c8484b14e68.jpg)
After connecting the device, don't forget to change your audio input source on the raspberry pi.<br>
You can change it with the help of the raspi config command in the terminal, and select your sound receiver from the opened list.

## 5) Run the entire program that includes the voice recognition model

The only program to run on the Raspberry Pi will be the wakeup.py program, which is located in the rosy folder.<br>
You can familiarize yourself with the program work with the notes written in the program, and here you will see a general description of the program.<br>

<b>General description

After giving the parameters of the screen, we import the model we have learned, which will differentiate the words.

We constantly record a 1-second audio tape in a "loop", which we change to a suitable appearance and give to our model.

First, we check whether the word to be heard, which is "marvel", is heard.
If that word is heard, then our model starts its work, if not, it waits until it is heard.
</b>

## The last step. <br>
Open a terminal in the rosy folder and run the wakeup.py program:</b>
`python wakeup.py`
