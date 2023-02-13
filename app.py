import sys
import time

DECOR = "----------------"

class Hero:
    """Main class to manage hero properties"""
    def __init__(self, name) -> None:
        self.name = name
        self.hp = 10
        self.inventory = []
        self.max_items = 2

    def show_inventory(self):
        """Simple showing inventory"""
        if self.inventory:
            print(f"Your inventory: {self.inventory}")
        else:
            print("Your inventory is empty.")

    def pick_item(self, item):
        """simple pick item"""
        if len(self.inventory) <= self.max_items:
            self.inventory.append(item)
            print(DECOR)
            print(f"You picked {item}.")
            print(DECOR)
        else:
            print("You don't have enough space in your inventory. Continue or remove some items.")

    def remove_item(self):
        """Simple removing items"""
        if self.inventory:
            item = input("What item do you want to remove? ")
            print(f"Your inventory: {self.inventory}")
            while item not in self.inventory:
                item = input("What item do you want to remove? ")
            self.inventory.remove(item)
        else:
            print("Your inventory is empty")

class Room:
    """Main class to manage room"""
    def __init__(self, room_name, room_desc, hero) -> None:
        self.room_name = room_name
        self.room_desc = room_desc
        self.hero = hero

    #riddle method
    def riddle(self):
        """Riddle method to enter the room"""
        with open('riddle.txt', 'r') as file:
            reader = file.readlines()
            riddle = reader[0].strip()
            answer = reader[1]
        print(riddle)
        user_answer = input("What is the answer (one word)? ").lower()
        while answer != user_answer:
            print("I'm so sorry, you tried, but you failed. Come back with correct answer!")
            continue_game = input("Do you want to try again (yes/no)? ").lower()

            while continue_game not in ['yes', 'y', 'n', 'no']:
                print("I don't know what you mean. Please try again.")
                continue_game = input("Do you want to try again (yes/no)? ").lower()

            if continue_game in ['n', 'no']:
                print("Okay then, come back anytime! Bye!")
                sys.exit(1)
            user_answer = input("What is the answer? (one word) ").lower()
        print(DECOR)
        print("Well done traveler! Come in!")
        time.sleep(1)
        Room.room_things(self)

    def room_things(self):
        """method to start play """
        print(f"{DECOR}")
        print(f"{self.room_desc}")
        print(f"{DECOR}")
        time.sleep(2)
        # List of 4 magical items
        magical_items = ["Ring of Power", "Magic Wand", "Amulet of Protection", "Crystal of Wisdom"]
        print("In this room, you find 4 magical items:")
        for item in magical_items:
            print(DECOR)
            print(item)
            print(DECOR)
        time.sleep(1)
        while True:
            print("What would you like to do?")
            print("1. Show Inventory")
            print("2. Pick Item")
            print("3. Remove Item")
            print("4. Leave Room and go home")
            print("5. Continue Exploring")
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                self.hero.show_inventory()
            elif choice == 2:
                if len(self.hero.inventory) < self.hero.max_items:
                    item = input("Which item would you like to pick? ")
                    while item not in magical_items:
                        print("Item not found in the room.")
                        item = input("Which item would you like to pick? ")
                    self.hero.pick_item(item)
                    magical_items.remove(item)
                else:
                    print("You can't pick more items, your inventory is full.")
            elif choice == 3:
                self.hero.remove_item()
            elif choice == 4:
                print("You decide to leave the dungeon and return to the safety of the village.")
                print("You get nothing, but you are alive. Your family is happy to see you again!")
                self.end()
                break
            elif choice == 5:
                self.continue_exploring()
            else:
                print("Invalid choice. Try again.")
            

    def continue_exploring(self):
        """method with various endings"""
        if "Ring of Power" in self.hero.inventory and "Amulet of Protection" in self.hero.inventory:
            print(DECOR)
            print("""You find a secret door and use the Ring of Power to unlock it.
            The Amulet of Protection helps you safely navigate through the traps and obstacles inside.""")
            print("You find a treasure trove filled with gold and jewels! You are now incredibly wealthy.")
            print("You didn't need to search anymore. You take treasure and go back home.")
            self.end()
        elif "Crystal of Wisdom" in self.hero.inventory and "Magic Wand" in self.hero.inventory:
            print(DECOR)
            print("You find a mysterious portal and use the Crystal of Wisdom to decipher the incantation needed to activate it.")
            print("You are transported to a magical realm where you are granted unlimited magical powers.")
            print("You teleported out of room and became the most known wizard in the world.")
            self.end()
        elif "Ring of Power" in self.hero.inventory or "Amulet of Protection" in self.hero.inventory:
            print(DECOR)
            print("You venture deeper into the dungeon and encounter a powerful monster.")
            print("But without both the Ring of Power and the Amulet of Protection, you are unable to defeat the monster and must retreat.")
            self.choices()
        else:
            print(DECOR)
            print("You venture deeper into the dungeon and soon become lost.")
            print("Without any magical items to aid you, you are unable to find your way back and eventually succumb to the dangers of the dungeon.")
            print("You ended in the worst case scenario. You died from dark and insanity!")
            self.end()
    
        
        
    def choices(self):
        """ Choices method extending continue_exploring """
        choice = input("Do you want to continue exploring the room or leave it? (continue/leave) ").lower()
        if choice == "continue":
            print("You decide to keep exploring the dungeon.")
            self.hero.hp = self.hero.hp - 10
            print("As you explore, you are hurt and lose 10 HP.")
            self.ending_choices()
        elif choice == "leave":
            print("You decide to leave the dungeon and return to the safety of the village.")
            print("You get nothing, but you are alive. Your family is happy to see you again!")
            self.end()
            
    def ending_choices(self):
        """Another endings"""
        choice = input("Do you want to search for a way out or keep exploring? (search/explore) ").lower()
        if choice == "search":
            print("You decide to search for a way out of the dungeon.")
            if self.hero.hp > 0:
                print("After a long search, you finally find the way out and escape the dungeon.")
                self.end()
            else:
                print("You are too injured from exploring and are unable to continue searching. You succumb to your injuries and die in the dungeon.")
        elif choice == "explore":
            print("You decide to keep exploring the dungeon.")
            if self.hero.hp > 0:
                print("You continue exploring the dungeon and eventually find another room filled with treasure.")
                print("You find a treasure trove filled with gold and jewels! You are now incredibly wealthy.")
                print("You didn't need to search anymore. You take treasure and go back home.")
                self.end()
            else:
                print("You are too injured from exploring and are unable to continue. You succumb to your injuries and die in the dungeon.")
                self.end()

    def end(self):
        """ Shows the end"""
        time.sleep(1)
        print(DECOR)
        print("The end. Thanks for playing.")
        sys.exit(1)

def play():
    """ starting function"""
    print("Welcome in my game!")
    hero_name = input("What's your name traveler? ").capitalize()
    hero = Hero(hero_name)
    with open('room_description.txt', 'r') as file:
        reader = file.readlines()
        room_name = reader[0]
        room_description = reader[1:]
    room_description = ''.join(room_description)
    room = Room(room_name, room_description, hero)
    room.riddle()

play()
