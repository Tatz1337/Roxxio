#imports
from colorama import Fore, Back, Style, init
init(convert=True)
print(Fore.GREEN + "Imported Colorama!")
import time
print("Imported Time!")
import os 
print("Imported OS!")
import numpy
print("Imported NumPY!")
import requests
print("Imported Requests!")
import pandas
print("Imported Pandas!")
import tensorflow
print("Imported TensorFlow!")
import scrapy
print("Imported Scrapy!")
import keras
print("Imported Keras!")
import flask
print("Imported Flask!")
import imageai
print("Imported ImageAI!")
import ctypes
print("Imported CTypes!")
# SETS TERMINAL TITLE TEXT
ctypes.windll.kernel32.SetConsoleTitleW("Roxx-IO")
import gtts
print("Imported gtts!")
from playsound import playsound
print("Imported Playsound!")
# END OF IMPORTS

# AI NAME AND LOGO PRINTING
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
comd = input("What can I do for you~? - ")

# TEST QUESTION + ANSWER
if comd in ['wru', "who are you", "who are you?", "who are ya?", "who are ya"]: 
	print ("I am " + name + "." + "    ^.^")