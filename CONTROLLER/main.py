#! /usr/bin/env python3
# coding: utf-8
from player import *
from program import *

if __name__ == "__main__":
    print("Hello start game")
    player = Player()
    #ask method name entry in player.py for entry name
    player.name_entry()
    # ask method for choice level of game
    player.level_choice()
    game = Program()
    play_again = True
    while play_again == True:
        numbers = None
        # ask method to use level in program
        game.get_level(player.level)
        # ask method random number
        game.random_choice()
        # ask method for save number in list
        game.add_list_choice()
        # method for clear prompt
        game.clear_terminal()
        # ask method for compare number user and program list
        if game.compare_list(player.player_numbers, numbers) == False:
            print("game over")
            break
    pursuite = Program()
    pursuite.play_again_choice()
    if play_again == True:
        print("replay.....")
            
        


