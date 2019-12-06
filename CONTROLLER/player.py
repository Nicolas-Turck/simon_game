import os
from time import sleep
from program import *
class Player:
    """method for initialyse name"""
    def __init__(self):
        self.name = ""
        self.level = None        
        self.player_numbers = 0
    
    """method for ask and save name entry"""
    def name_entry(self):
        name = input("enter your name  :")
        if name == "":
            name = "GHOST"
        self.name = name.upper()
    
    def level_choice(self):
        """method for user choice level"""
        level = ""
        while level != "1" and level != "2" and level != "3":
            level = input("...{} enter number of difficulty choice\n 1:easy 2:midle 3:hard\n".format(self.name))
        self.level = int(level)
        print("{} you choice level {} start game ..........".format(self.name,level))
        sleep(2)
        os.system("clear")
        return level
    
    """ def player_entry(self):
            save number entry user 
        self.player_numbers = int(input("enter numbers......:"))
        player_numbers = self.player_numbers
        #game.compare_list(player_numbers, result_lists)
        return player_numbers"""
        
