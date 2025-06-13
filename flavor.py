class Flavor:

# base class for all flavors
    def __init__(self,name,heat_level):
        # setting name and spice level
        self.name = name
        self.heat_level = heat_level

    def __str__(self):
        # displays flavor name and heat level when printed
        return self.name + "(Heat Level: " + str(self.heat_level) + ")"
    
    def match_score(self, answers):
        # child classes will implement their own version of this method
        raise NotImplementedError("Subclasses must implement match_score")

    def personality(self):
        # basic personality description for a flavor
        return "This flavor has a unique personality."
