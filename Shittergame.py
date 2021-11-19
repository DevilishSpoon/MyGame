import random
import time
from os import system, name

def clearscreen():
    if name == "nt": _ = system("cls")
    else: _ = system("clear")

def main():
    menu_choice = None
    while menu_choice != ("0"):
        menu_choice = input("Agrababuptis")

class player:
    def __init__(self, player_name):
        self.name = player_name
        self.stats = {
        "Level":7,
        "Vigor":1,
        "Perseverence":1,
        "Endurance":1,
        "Strength":1,
        "Dexterity":1,
        "Intelligence":1,
        "Faith":1,
        }
        self.maxhealth = self.stats["Vigor"]*5
        self.health = self.maxhealth
        self.inventory = [ ]
        self.gold = 0
        self.status = []
    def __pass_time(self):
        if self.status == True:
            if "poison" in self.status:
                self.health -= 1
    def view_level(self):
        temp_list = (self.stats.keys())
        ret_str = """\n___________________________"""
        for item in temp_list:
            ret_str += f"\n{item:<16}|\t{self.stats[item]}"
        ret_str += """\n___________________________"""
        return ret_str
    def level_up(self):
        print(view_level())
        item_levelup = input("What would you like to level up")



shitter = player("What's your name?")
print(shitter)
