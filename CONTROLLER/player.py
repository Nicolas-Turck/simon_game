class Player:
    """method for initialyse name"""
    def __init__(self):
        self.name = None 
        self.level = None
        
    """method for ask and save name entry"""
    def name_entry(self):
        name = ""
        while name == "":
            name=input("...enter your name :")
        self.name = name
    
    def level_choice(self):
        """method for user choice level"""
        level = ""
        while level != "1" and level != "2" and level != "3":
            level = input("...{} enter number of difficulty choice\n 1:easy 2:midle 3:hard\n".format(self.name))
        self.level = level
        print("{} you choice level {} start game ..........".format(self.name, self.level))
