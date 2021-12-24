#imports
import gtts
print("Imported gtts!")
from io import BytesIO
print("Imported BytesIO!")
from playsound import playsound
print("Imported Playsound!")

# Little bit of ByteIO magic before end of imports!
from colorama import Fore, Back, Style, init
init(convert=True)
print(Fore.GREEN + "Imported Colorama!")
tts = gtts.gTTS("Imported Colorama!")
tts.save("colorama_import.mp3")
playsound("colorama_import.mp3")
import time
print("Imported Time!")
tts = gtts.gTTS("Imported Time!")
tts.save("time_import.mp3")
playsound("time_import.mp3")

import os 
print("Imported OS!")
tts = gtts.gTTS("Imported OS!")
tts.save("os_import.mp3")
playsound("os_import.mp3")

import numpy
print("Imported NumPY!")
tts = gtts.gTTS("Imported Numb Pie!")
tts.save("numpy_import.mp3")
playsound("numpy_import.mp3")

import requests
print("Imported Requests!")
tts = gtts.gTTS("Imported Requests!")
tts.save("import1.mp3")
playsound("import1.mp3")

import pandas
print("Imported Pandas!")
tts = gtts.gTTS("Imported Pandas!")
tts.save("import2.mp3")
playsound("import2.mp3")

import tensorflow
print("Imported TensorFlow!")
tts = gtts.gTTS("Imported Tensor Flow!")
tts.save("import3.mp3")
playsound("import3.mp3")

import scrapy
print("Imported Scrapy!")
tts = gtts.gTTS("Imported Scrape e!")
tts.save("import4.mp3")
playsound("import4.mp3")

import keras
print("Imported Keras!")
tts = gtts.gTTS("Imported Keras!")
tts.save("import5.mp3")
playsound("import5.mp3")

import flask
print("Imported Flask!")
tts = gtts.gTTS("Imported Flask!")
tts.save("import6.mp3")
playsound("import6.mp3")

import imageai
print("Imported ImageAI!")
tts = gtts.gTTS("Imported Image AI!")
tts.save("import7.mp3")
playsound("import7.mp3")

import ctypes
print("Imported CTypes!")
tts = gtts.gTTS("Imported C types!")
tts.save("import8.mp3")
playsound("import8.mp3")

# SETS TERMINAL TITLE TEXT
ctypes.windll.kernel32.SetConsoleTitleW("Roxx-IO")
# END OF IMPORTS

# NOT IMPLEMENTED LIST 
#tts = gtts.gTTS("Password Cracking, Facial Recognition, Voice Cloning, Facial Swapping, Universal Autopilot, Personality Data, Internet Relay Chat, AI learning, Airplay,  Saving have all not been implemented yet!")
#tts.save("import12.mp3")
#playsound("import12.mp3")
# END OF LIST
# AI NAME AND LOGO PRINTING


dir_name = "C:/Users/mysti/Desktop/Roxxio"
test = os.listdir(dir_name)

for item in test: 
	if item.endswith(".mp3"): 
		os.remove(os.path.join(dir_name, item))


name = "Roxx-IO"
print(Style.RESET_ALL)
with open('roxlogo.txt', 'r') as f:
    for line in f:
        print(line.rstrip())
# END OF LOGO PRINTING

# CHANGE FROM GREEN IMPORTING TEXT COLOR TO NORMAL WHITE
print(Style.RESET_ALL)

# CHECK IF ONLINE
url = "http://www.kite.com"
timeout = 5
request = requests.get(url, timeout=timeout)
print("I am " + Fore.GREEN + "online!")
# END OF ONLINE CHECK

# RESET FROM GREEN TEXT FOR ONLINE STATUS BACK TO WHITE
print(Style.RESET_ALL)

# INPUT PROMPT
tts = gtts.gTTS("I am rocks I O... I am connected to the internet. What can I do for you?")
tts.save("hello.mp3")
playsound("hello.mp3")
comd = input("Input Command - ")

# TEST QUESTION + ANSWER
if comd in ['wru', "who are you", "who are you?", "who are ya?", "who are ya"]: 
	print ("I am " + name + "." + "    ^.^")