#! /usr/bin/env python3
# coding: utf-8
from player import *
from program import *
from player_game import *

if __name__ == "__main__":
    print("Hello start game")
player = Player()
#ask method name entry in player.py
player.name_entry()
#ask method level choice for user select level
player.level_choice()
game = Program()
#ask method to use level in program
game.get_level(player.level)
#ask method random number 
game.random_choice()
#ask method for save number in list
game.add_list_choice()
#method for clear prompt
game.clear_terminal()
player_game = Player_entry()
#ask method for player entry number 
player_game.player_entry()
#method for add to list number of user entry
player_game.add_user_list()

print(Player_entry)
print(player_game.__dict__)
#method for compare list player and program list
game.compare_list(player_game.player_list)

