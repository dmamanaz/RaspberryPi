{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red67\green158\blue79;\red249\green245\blue242;}
{\*\expandedcolortbl;;\cssrgb\c31765\c67059\c38431;\cssrgb\c98039\c96863\c96078;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
#!/usr/bin/python\
\
\
\
import os\
\
from time import sleep\
\
import RPi.GPIO as GPIO\
\
\
\
GPIO.setmode(GPIO.BCM)\
\
\
\
# setup our input pin\
\
# we use an internal pull up resistor to hold the pin at 3v3, otherwise the inputs value could chatter between high and low\
\
\
\
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)\
\
\
\
while True:\
\
    if ( GPIO.input(10) == False ):\
\
        print("Button Pressed")\
\
        os.system('date') # print the systems date and time\
\
        print GPIO.input(10)\
\
        sleep(5)\
\
    else:\
\
        os.system('clear') # clear the screens text\
\
        print ("Waiting for you to press a button")\
\
        sleep(0.1)}