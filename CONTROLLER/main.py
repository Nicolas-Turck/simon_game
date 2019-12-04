#! /usr/bin/env python3
# coding: utf-8
from player import *
from program import*

if __name__ == "__main__":
    print("Hello start game")
player = Player()
#ask method name entry in player.py
player.name_entry()
#ask method level choice for user select level
player.level_choice()
#show name and choice user

#ask method for display choice game of user
#show_information.display_name_choice()