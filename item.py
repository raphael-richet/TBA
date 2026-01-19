# Description: Item class

class Item:
    """
    Class to represent an object that can be found in rooms.
    
    Attributes:
        name (str): The name of the object
        description (str): The description of the object
        weight (int): The weight of the object in kg
    """
    
    def __init__(self, name, description, weight):
        """
        Initialize an Item.
        
        Parameters:
            name (str): The name of the object
            description (str): The description of the object
            weight (int): The weight of the object in kg
        """
        self.name = name
        self.description = description
        self.weight = weight
    
    def __str__(self):
        """
        Return a textual representation of the object.
        
        Returns:
            str: A formatted string with the name, description, and weight
            
        Example:
            sword : a sword with a razor-sharp edge (2 kg)
        """
        if self.weight == 0:
            return f"{self.name} : {self.description}"
        return f"{self.name} : {self.description} ({self.weight} kg)"
