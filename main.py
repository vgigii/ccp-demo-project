from atomic import Atomic
from cajun import Cajun

# create a list of available flavor objects
flavors = [Atomic(), Cajun()]

# ask the user some personality-style questions
print("Welcome to the Wingstop Flavor Quiz!")
print("Answer the following questions with one word:")
print("Choose from: bold, fun, chill")

# collect answers from the user
answers = []
answers.append(input("How would your friends describe you? "))
answers.append(input("What do you prefer to do on the weekend? "))
answers.append(input("Pick a mood for your ideal summer: "))

# Find the best matching flavor
best_flavor = None
highest_score = -1

for flavor in flavors:
    score = flavor.match_score(answers)
    if score > highest_score:
        highest_score = score
        best_flavor = flavor

# Show the result
print("")
print("Your Wingstop Flavor Match is:")
print(best_flavor)
print(best_flavor.personality())
