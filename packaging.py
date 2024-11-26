class Packaging:
    def __init__(self):
        self.packaging = None
        if isinstance( self , Candy):
            self.packaging = "Bag"
        elif isinstance(self , Cookie):
            self.packaging = "Box"
        elif isinstance(self , IceCream):
            self.packaging = "Bowl"
        elif isinstance(self , Sundae):
            self.packaging = "Boat"