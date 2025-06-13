from flavor import Flavor

# this class represents spicy flavors, which are a type of Flavor
class SpicyFlavor(Flavor):
    def __init__(self, name, heat_level):
        # call the parent (Flavor) constructor
        super(SpicyFlavor, self).__init__(name, heat_level)

    def personality(self):
        return "You're bold, exciting, and a little dangerous—just like a spicy flavor!"

