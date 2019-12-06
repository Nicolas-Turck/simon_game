from random import *
import os
from time import sleep

class Program:
    """class for program controller """
    def __init__(self):
        self.program_list = []
        self.numbers_program = None
        self.number_user = 0
        self.level_choice = None
        # self.result_lists = None

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
    
    def compare_list(self, player_numbers, program_lists):
        """compare list user and list program """
        #player_numbers = int(input("enter numbers ......:"))
        for i in self.program_list:
            player_numbers = int(input("enter numbers ......:"))
            if player_numbers == i:
                print("good number next")
               
            if player_numbers != i:
                break
                
    def play_again():
        """ask to player if his play again"""
        while play_again_choice != "yes" and play-again != "no":
            play_again_choice = input("do you want to play again enter yes or no :")
            if play_again_choice == "yes":
                __name__ == "__main__"
            else:
                break
    
    
   