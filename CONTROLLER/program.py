from player import *
from player_game import *
from random import *
import os
class Program:
    """class for program controller """
    def __init__(self):
        self.program_list = []
        self.user_list = []
        self.numbers_program = None
        self.number_user = 0
    
    def random_choice(self):
        """method for choice random number """
        self.numbers_program = randrange(1, 100)
        print(self.numbers_program)
        
    def add_list_choice(self):
        """add to empty list number choice"""
        self.program_list.append(self.numbers_program)
        print(self.program_list)
    
    def clear_terminal(self):
        """method for clear prompt after disaplay number"""
        os.system("clear")
    
    

    def compare_list(self):
        """compare list user and list program """
        if self.user_list == self.program_list:
            print("True")
        else:
            print("false")


    def clear_user_list():
        """clear user list number for again manche"""
   
    def play_again():
        """ask to player if his play again"""
    
    
    