import random
import time
from os import system, name

MENU = """
\t\tSHITTER GAME
_______________________________________
1 - View Level
2 - Level Up
3 - View Inventory
0 - Quit
\t

"""
def clearscreen():
    if name == "nt": _ = system("cls")
    else: _ = system("clear")


def main(shitter):
    menu_choice = None
    while menu_choice != ("0"):
        clearscreen()
        print(MENU)
        menu_choice = input("Agrababuptis")
        if menu_choice in ("1","2","3"):
            if menu_choice == "1":
                print(shitter.view_level())
                time.sleep(5)
            elif menu_choice == "2":
                print(shitter.level_up())
                time.sleep(2)
            elif menu_choice == "14":
                shitter = player("What's your name?")

class player:
    def __init__(self, player_name):
        self.name = player_name
        self.stats = {
        "Level":7,
        "Vigor":1,
        "Soul":1,
        "Endurance":1,
        "Strength":1,
        "Dexterity":1,
        "Intelligence":1,
        "Faith":1,
        }
        self.maxhealth = self.stats["Vigor"]*5
        self.health = self.maxhealth
        self.inventory = [ ]
        if self.name == "God's Plan": self.gold = 100000
        else: self.gold = 0
        self.status = []
    def __pass_time(self):
        if self.status == True:
            if "poison" in self.status:
                self.health -= 1
    @property
    def levelcost(self):
        levelcost = 75*(self.stats["Level"])
        return levelcost
    def view_level(self):
        temp_list = (self.stats.keys())
        ret_str = """\n___________________________"""
        for item in temp_list:
            ret_str += f"\n{item:<16}|\t{self.stats[item]}"
        ret_str += """\n___________________________\n75*Level to level up once\n___________________________"""
        return ret_str
    def level_up(self):
        print(self.view_level())
        print(self.display_gold())
        stat_levelup = input("\nWhat would you like to level up?\n").capitalize()
        if stat_levelup not in self.stats:
            return f"{stat_levelup} is not a valid attribute."
        times_level = input("\nHow many times would you like to level?\n")
        if times_level.isdigit() == False:
            return f"{times_level} is not an integer."
        return self.__statsup(stat_levelup, times_level)
    def __statsup(self, stat_levelup, times_level):
        actual_levelup = 0
        gold_spent = 0
        for i in range(int(times_level)):
            if self.gold-self.levelcost > 0:
                self.gold -= self.levelcost
                self.stats[stat_levelup] += 1
                self.stats["Level"] += 1
                actual_levelup += 1
                gold_spent += self.levelcost
            else: return f"Leveled up {actual_levelup} times and spent {gold_spent}"
        return f"Leveled up {actual_levelup} times and spent {gold_spent}"
    def display_gold(self):
        return f"""___________________________\n\tGold: {self.gold}\n___________________________"""

shitter = player(input("What's your name?"))
main(shitter)
