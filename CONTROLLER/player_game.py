from program import *
class Player_entry:
    """class for player entry and list for compare with program list"""
    def __init__(self):
        self.player_list = []
        self.player_numbers = 0

    def player_entry(self):
        """save number entry user """
        player_numbers = int(input("enter numbers ......:"))
        self.player_numbers = player_numbers
        
    def add_user_list(self):
        """save in list number entry user"""
        #print(self.player_list)
        self.player_list.append(self.player_numbers)
        player_list = self.player_list
        #print(player_list)
        return player_list
        
        
        

        
        
        
        