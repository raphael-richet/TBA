"""
Class `Room`.

Represents a room on the map, its exits, its inventory, and the characters present.
"""

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}  # NPCs present in the room

    def get_exit(self, direction):
        """Return the room in the given direction or `None`."""
        return self.exits.get(direction, None)

    def get_exit_string(self):
        """Return a string listing the exits of the room."""
        exit_string = "Sorties: "
        for e in self.exits.keys():
            if self.exits.get(e) is not None:
                exit_string += e + ", "
        return exit_string.strip(", ")

    def get_long_description(self):
        """Long description of the room, including exits."""
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """Return a string describing the objects present in the room."""
        if len(self.inventory) == 0:
            return "\nIl n'y a rien ici.\n"
        result = "\nOn voit:\n"
        for item in self.inventory.values():
            result += f"    - {item}\n"
        result += "\n"
        return result
