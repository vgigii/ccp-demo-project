from spicyflavor import SpicyFlavor

# the cajun flavor is spicy and fun
class Cajun(SpicyFlavor):
    def __init__(self):
        # give it a name and a medium heat level
        super(Cajun, self).__init__("Cajun", 3)

    def match_score(self, answers):
        # the more "fun" the answers are, the better the match
        return answers.count("fun") + self.heat_level

