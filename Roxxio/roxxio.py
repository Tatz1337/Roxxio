from colorama import Fore, Back, Style
print("Imported Colorama!")
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
ctypes.windll.kernel32.SetConsoleTitleW("Roxx-IO")
name = "Roxx-IO"



with open('roxlogo.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

print("Standing by for your command!")
time.sleep(5)

comd = input("What can I do for you? - ")

if comd in ['wru', "who are you", "who are you?", "who are ya?", "who are ya"]: 
	print ("I am " + name + "." + "    ^.^")