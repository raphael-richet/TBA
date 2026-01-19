# Description: Character class for NPCs

import random

import game

class Character:
    """
    Class to represent a non-player character (NPC).
    
    Attributes:
        name (str): The name of the character
        description (str): The description of the character
        current_room (Room): The current room of the character
        msgs (list): The list of messages the character can say
    """
    
    def __init__(self, name, description, current_room, msgs):
        """
        Initialize a Character.
        
            Parameters:
                name (str): The name of the character
                description (str): The description of the character
                current_room (Room): The current room of the character
                msgs (list): The list of messages the character can say
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs[:]  # copy of the messages list
        self._msg_index = 0  # to track which message to display
        # Optional list of rooms (Room objects) where this NPC is allowed to go.
        # None means no restrictions (can go anywhere).
        self.allowed_rooms = None
    
    def __str__(self):
        """
        Return a textual representation of the character.
        
            Returns:
            str: A string in the format "name : description"
        """
        return f"{self.name} : {self.description}"
    
    def get_msg(self):
        """
        Return messages from the NPC cyclically.

            Returns:
            str: The formatted NPC message
        """
        if not self.msgs:
            return f"{self.name} ne dit rien..."
        msg = self.msgs[self._msg_index]
        self._msg_index = (self._msg_index + 1) % len(self.msgs)
        return f"\n{self.name} : {msg}\n"
    
    def move(self):
        """
        The NPC has a 50% chance to move to an adjacent room.

            Returns:
            bool: True if the NPC moved, False otherwise
        """
        # Only allow movement for the 'Durand' NPC
        if self.name != "Durand":
            return False

        # If an authorization list is defined, only attempt the random draw
        # (50% chance) if the NPC is in an authorized room.
        if self.allowed_rooms is not None and self.current_room not in self.allowed_rooms:
            return False

        if random.choice([True, False]):
            exits = [room for room in self.current_room.exits.values() if room is not None]
            # If an authorization list is defined, only keep authorized exits.
            # If no authorized exit is present, the NPC does not move.
            if self.allowed_rooms is not None:
                allowed_set = set(self.allowed_rooms)
                allowed_exits = [r for r in exits if r in allowed_set]
                if allowed_exits:
                    exits = allowed_exits
                else:
                    return False
            if exits:
                new_room = random.choice(exits)
                if game.DEBUG:
                    print(f"DEBUG: {self.name} moves to {new_room.name}")
                self.current_room.characters.pop(self.name, None)
                self.current_room = new_room
                self.current_room.characters[self.name] = self
                return True
        return False
