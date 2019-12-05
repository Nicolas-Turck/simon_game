from random import *
import os
from time import sleep
from player_game import *
class Program:
    """class for program controller """
    def __init__(self):
        self.program_list = []
        self.user_list = []
        self.numbers_program = None
        self.number_user = 0
        self.level_choice = None

    def get_level(self, level):
        self.level_choice = level
        print(self.level_choice)
        
    def random_choice(self):
        """method for choice random number """
        if self.level_choice == 3:
            self.numbers_program = randrange(1, 100)
            print(self.numbers_program)
            sleep(1)
        if self.level_choice == 2:
            self.numbers_program = randrange(1, 20)
            print(self.numbers_program)
            sleep(2)
        if self.level_choice == 1:
            self.numbers_program = randrange(1, 10)
            print(self.numbers_program)
            sleep(3)
        
    def add_list_choice(self):
        """add to empty list number choice"""
        self.program_list.append(self.numbers_program)
        #print(self.program_list)
            

    def clear_terminal(self):
        """method for clear prompt after disaplay number"""
        os.system("clear")
    
    def compare_list(self, player_list):
        """compare list user and list program """
        if player_list == self.program_list:
            print("True")
        else:
            print("false")

    def clear_user_list():
        """clear user list number for again manche"""
   
    def play_again():
        """ask to player if his play again"""
    
    
    