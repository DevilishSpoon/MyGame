import random
import time
from os import system, name

def clearscreen():
    if name == "nt": _ = system("cls")
    else: _ = system("clear")

def main():
