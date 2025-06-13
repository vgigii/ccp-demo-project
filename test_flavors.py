from atomic import Atomic
from cajun import Cajun

# sample answers
answers = ["bold", "fun", "bold"]

# create flavor objects
atomic = Atomic()
cajun = Cajun()

# check their scores
print("Atomic score: " + str(atomic.match_score(answers)))  # Should be 2 "bold" + 5 = 7
print("Cajun score: " + str(cajun.match_score(answers)))    # Should be 1 "fun" + 3 = 4

# basic test
if atomic.match_score(answers) > cajun.match_score(answers):
    print("Test passed: Atomic wins.")
else:
    print("Test failed: Cajun shouldn't win.")
