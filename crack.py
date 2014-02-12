import sys
import time
import os
import random   #Random numbers
import re       #Regular expressions
from sys import *


# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray


capFile = argv[1] #Location of capture file. First argument.

def menu(capture):
    os.system("clear") 
    print(R+"Attempting to crack WEP with capture file "+capture+W)
    print("")
    os.system("airocrack-ng") 

def wepCrack(capture):
    print(capture)


def wpaCrack():
    print("WPA Crack here")



menu(capFile)
wepCrack(capFile)
