from player import *
from random import *
class Program:
    """class for program controller """
    def __init__(self):
        self.program_list = []
        self.user_list = []
        self.numbers_program = None
    
    def random_choice(self):
        """method for choice random number """
        self.numbers_program = randrange(1, 100)
        print(self.numbers_program)
        
    def add_list_choice(self):
        """add to empty list number choice"""
        self.program_list.append(self.numbers_program)
        print(self.program_list)
    
    def clear_terminal():
        """method for clear prompt after disaplay number"""
    
    def player_entry():
        """save number entry user """
    
    def add_user_list():
        """save in list number entry user"""

    def compare_list():
        """compare list user and list program """

    def clear_user_list():
        """clear user list number for again manche"""
   
    def play_again():
        """ask to player if his play again"""
    
    
    