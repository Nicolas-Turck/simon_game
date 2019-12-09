from random import *
import os
from time import sleep
from player import *
from main import *

class Program:
    """class for program controller """
    
    """method for initialyse many attibutes """
    def __init__(self):
        self.program_list = []
        self.numbers_program = None
        self.number_user = 0
        self.level_choice = None
        self.play_again = None
        self.player_numbers = 0
        

    def get_level(self, level):
        """method for save level choice user"""
        self.level_choice = level
        
    def random_choice(self):
        """method for choice random number """
        if self.level_choice == 3:
            # select number betwen 1 and 100 
            self.numbers_program = randrange(1, 100)
            
        if self.level_choice == 2:
            # select number betwen 1 and 20
            self.numbers_program = randrange(1, 20)
            
        if self.level_choice == 1:
            # select number between 1 and 10
            self.numbers_program = randrange(1, 10)
            
    def add_list_choice(self):
        """add to empty list number choice"""
        self.program_list.append(self.numbers_program)
            
    def clear_terminal(self):
        """method for clear prompt after display number"""
        if self.level_choice == 1:
            for  i in self.program_list:
                print("> {}".format(i))
                sleep(3)
                os.system("clear")
            
        if self.level_choice == 2:
            for i in self.program_list:
                print("> {}".format(i))
                sleep(2)
                os.system("clear")
            
        if self.level_choice == 3:
            for i in self.program_list:
                print("> {}".format(i))
                sleep(1)
                os.system("clear")
    
    def compare_list(self):
        """compare list user and list program """
        for i in self.program_list:
            self.player_numbers = self.player_numbers_entry()
        if self.player_numbers != i:
            self.program_list = []
            return False
        
    def player_numbers_entry(self):
        """method for verify if number is an integer"""
        while True:
            try:
                self.player_numbers = int(input("enter numbers........:"))
            except:
                print("not good")
                continue
            return self.player_numbers

    def play_again_choice(self):
        """ask to player if his play again"""
        while self.play_again != "yes" or self.play_again != "no":
            self.play_again = input("do you want to play again enter yes or no :")
            if self.play_again == "yes":
                self.program_list = []
                return self.play_again
                

            else:
                print("good bye")
                exit()
    
    
   