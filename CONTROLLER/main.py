#! /usr/bin/env python3
# coding: utf-8
from player import *
from program import *

if __name__ == "__main__":
    print("Hello start game")
    player = Player()
    #ask method name entry in player.py
    player.name_entry()
    #ask method level choice for user select level
    player.level_choice()
    game = Program()
    #result_lists = True
    restart = True
    result_lists = True
    while result_lists != False:
        # ask method to use level in program
        game.get_level(player.level)
        # ask method random number
        game.random_choice()
        # ask method for save number in list
        game.add_list_choice()
        # method for clear prompt
        game.clear_terminal()
        # ask method for compare number user and program list
        game.compare_list(player.player_numbers, result_lists)

    #if result_lists == False:
        #game.play_again_choice()
    if restart == True:
        __name__ == "__main__"


