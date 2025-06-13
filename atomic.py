from spicyflavor import SpicyFlavor

# the atomic flavor is a very spicy option
class Atomic(SpicyFlavor):
    def __init__(self):
        # give it a name and a high heat level
        super(Atomic, self).__init__("Atomic", 5)

    def match_score(self, answers):
        # the more "bold" the answers are, the better the match
        return answers.count("bold") + self.heat_level
