"""
Author:         Landon Thomas
Date:           11/7/23
Assignment:     Lab 08
Course:         CPSC1051
Lab Section:    004

CODE DESCRIPTION:
This program models a person's text navigation through a fictional house.
The house has rooms stored in a dictionary that is modified and displayed by use of classes.
The user will select which room they would like to enter and the program will validate that 
the room is a potential exit, and will also take that user to that room.
"""





#class created to display an invalid exit
class ExitNotFoundError:
    def __init__(self, message = 'room not found'):
        self.message = message
    def __str__(self,exit):
        return f"{exit} -> {self.message}"
#define the room class to hold a room's description, name, and exits
class Room:
    #initializes code, gets the name, description, and exits, and also returns the room in a string.
    def __init__(self, name = '', description = '', exits = []):
        self.name = name
        self.description = description
        self.exits = exits
        self.str_exit = ''
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_exits(self):
        return self.exits
    def list_exits(self):
        for room in self.exits:
            self.str_exit += str(room)
            self.str_exit += '\n'
        return self.str_exit       
    def __str__(self):
        room_des = f"{self.name}: {self.description}\n\nExits:\n{self.str_exit}"
        return room_des
        
#define the adventuremap class that holds a dictionary of all rooms in the house
class AdventureMap:
    #initializes the map, defines how to add a room and go to a room in the map.
    def __init__(self, room = Room(), error = ExitNotFoundError()):
        self.map = {}
        self.error = error
        self.room = room
    def add_room(self, room_layout):
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
    def get_room(self, user_room):
        key_list = list(self.map.keys())
        count = 0
        for key in key_list:
            if user_room.lower() == key.lower():
                return self.map[key]
                user_room = key
                count += 1
    def main():
        #how the code will be displaed on the screen
        adventure_map = AdventureMap()
        print("\nWelcome to the Adkins house! Entering the study room. To leave the house, please type exit to jump out of the nearest window.\n")
        adventure_map.add_room(Room("Guest Room", "A room filled with numerous torture devices. Who said anything about welcome guests?", ['Kitchen']))
        adventure_map.add_room(Room("Library", "Better version of the study. It has all of the different books that one may want. Make sure that you stay quiet or the mean librarian will slap you!", ["Holodeck", "Trophy Room", "Study"]))
        adventure_map.add_room(Room("Kitchen", "This amazing culinary art studio has it all: cheese cellar, wine racks, and a 16 stove burner. With its pizza oven, it makes for the perfect Italian getaway.", ["Study", "Guest Room"]))
        adventure_map.add_room(Room("Study", "Do you love being disturbed while working? This room has it all. It is the central hub to the whole house. It has a giant wall of computers and amazing lighting, but doors that exit out into numerous different rooms.", ["Kitchen", "Library", "Bedroom"]))
        adventure_map.add_room(Room("Holodeck", "A room that can disguise itself in a variety of ways. Experience a lush, humid rainforest, a speakeasy of the 1920’s, or the dungeons of Cooper Library.", ["Library"]))
        adventure_map.add_room(Room("Trophy Room", "Spacious room with oak wood as far as the eye can see, shelves filled to the brim with trophies and obscure collections, it really makes you wonder who they belong to.", ["Bedroom", "Library"]))
        adventure_map.add_room(Room("Bedroom", "A lavished bed adorns the center of this room, with long curtains, beautiful rugs, and gilded furniture acting as little details to truly make this a great bedroom.", ["Study", "Trophy Room"]))
        print(adventure_map.get_room('Study'))
        play = True
        user_room_choice = 'study'
        while play:
            print("Please choose an exit:")
            user_choice = input().strip().lower()
            if user_choice == 'exit':
                print("Exiting the house out of the nearest window... thanks for the tour!")
                break
            if user_room_choice == 'study' and (user_choice.lower().strip() == "kitchen" or user_choice.lower().strip() == "library" or user_choice.lower().strip() == 'bedroom'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'guest room' and (user_choice.lower().strip() == 'kitchen'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'library' and (user_choice.lower().strip() == 'holodeck' or user_choice.lower().strip() == 'trophy room' or user_choice.lower().strip() == 'study'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'kitchen' and (user_choice.lower().strip() == 'study' or user_choice.lower().strip() == 'guest room'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'holodeck' and (user_choice.lower().strip() == 'library'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'trophy room' and (user_choice.lower().strip() == 'bedroom' or user_choice.lower().strip() == 'library'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            elif user_room_choice == 'bedroom' and (user_choice.lower().strip() == 'study' or user_choice.lower().strip() == 'trophy room'):
                print(adventure_map.get_room(user_choice))
                user_room_choice = user_choice
            else:
                print(f"{ExitNotFoundError().__str__(user_choice)}\n")

#run the code through main
if __name__ == "__main__":
    AdventureMap.main()

            
