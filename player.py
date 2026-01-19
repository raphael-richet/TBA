# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction, None)

        # If the next room is None, display an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        self.history.append(self.current_room)
        print(self.current_room.get_long_description())
        return True

    def get_inventory(self):
        """
        Return a string representing the player's inventory.
        
        Returns:
            str: The string representing the inventory
        """
        if len(self.inventory) == 0:
            return "\nVotre inventaire est vide.\n"
        
        result = "\nVous disposez des items suivants:\n"
        for item in self.inventory.values():
            result += f"    - {item}\n"
        result += "\n"
        return result
