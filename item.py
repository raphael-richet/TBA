# Description: Classe Item

class Item:
    """
    Classe pour représenter un objet qui peut être trouvé dans les pièces.
    
    Attributs:
        name (str): Le nom de l'objet
        description (str): La description de l'objet
        weight (int): Le poids de l'objet en kg
    """
    
    def __init__(self, name, description, weight):
        """
        Initialise un Item.
        
        Args:
            name (str): Le nom de l'objet
            description (str): La description de l'objet
            weight (int): Le poids de l'objet en kg
        """
        self.name = name
        self.description = description
        self.weight = weight
    
    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.
        
        Returns:
            str: Une chaîne formatée avec le nom, la description et le poids
            
        Exemple:
            sword : une épée au fil tranchant comme un rasoir (2 kg)
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
