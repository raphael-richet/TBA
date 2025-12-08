# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Retourne une chaîne représentant l'inventaire de la pièce.
        
        Returns:
            str: La chaîne représentant l'inventaire
        """
        if len(self.inventory) == 0:
            return "\nIl n'y a rien ici.\n"
        
        result = "\nOn voit:\n"
        for item in self.inventory.values():
            result += f"    - {item}\n"
        result += "\n"
        return result
