# number of mcq questions = 20
n = 20
#each question has four options, out of which one is correct
#probability of correct answer = 1/4
p = 1/4

# person answering 5 questions wrong = 15 questions correct
k = 15

from scipy.stats import binom
print(binom.pmf(15,20,p))
