#Import the necessary Packages and scritps for this software to run (Added speak in
#there too as an easer egg)
#define BLYNK_TEMPLATE_ID "TMPL58WD0kGr"
#define BLYNK_DEVICE_NAME "Quickstart Template"
import cv2
from collections import Counter
from module import findnameoflandmark,findpostion,speak
import math
import RPi.GPIO as GPIO
import time
import requests

def bulb1(): #pin 3 and pin 9
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,GPIO.OUT)
#print "LED on"
    GPIO.output(2,GPIO.HIGH)
    time.sleep(1)
#print "LED off"
    GPIO.output(2,GPIO.LOW)
    
def bulb2(): #pin 5 and pin6 
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(3,GPIO.OUT)
        #print "LED on"
    GPIO.output(3,GPIO.HIGH)
    time.sleep(1)
        #print "LED off"
    GPIO.output(3,GPIO.LOW)
        
def delay():
   time.sleep(1) 



#Use CV2 Functionality to create a Video stream and add some values + variables
cap = cv2.VideoCapture(0)
tip=[4,8,12,16,20]
tipname=[4,8,12,16,20]
fingers=[]
finger=[]

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
while True:
     ret, frame = cap.read() 
     #Unedit the below line if your live feed is produced upsidedown
     #flipped = cv2.flip(frame, flipCode = -1)
     
     #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
     frame1 = cv2.resize(frame, (640, 480))
    
    #Below is used to determine location of the joints of the fingers 
     a=findpostion(frame1)
     b=findnameoflandmark(frame1)
     
     #Below is a series of If statement that will determine if a finger is up or down and
     #then will print the details to the console
     # Thumb
     if a[[0]][1] > [[0] - 1][1]:
         fingers.append(1)
     else:
         fingers.append(1)
         
     if len(b and a)!=0:
        finger=[]
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
           print (b[4])
          
        else:
           finger.append(0)   
        
        fingers=[] 
        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               print(b[tipname[id]])

               fingers.append(1)
    
            else:
               fingers.append(0)
     #Below will print to the terminal the number of fingers that are up or down          
     x=fingers + finger
     c=Counter(x)
     up=c[1]
     down=c[0]
     
     while up==1:
         bulb1()
         print("1")
         break
     while up==2:
         bulb2()
         print("2")
         break
     while up==3:
         bulb1()
         bulb2()
         print("3")
         break
     while up==4: 
        bulb2()
        delay()
        bulb2()
        print("4")
        break
     while up==5:
         bulb1()
         delay()
         bulb1()
         print("5")
         break
         #that red i
     #print('This many fingers are up - ', up)
     #print('This many fingers are down - ', down)
     
     #Below shows the current frame to the desktop 
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
     
     
     #Below will speak out load when |s| is pressed on the keyboard about what fingers are up or down
     #if up=c[1]:
         
     
     #Below states that if the |s| is press on the keyboard it will stop the system
     if key == ord("s"):
       break
           
