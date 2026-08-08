#Find the probability of more than 6 heads from 10 fair coin flips using CDF
import scipy.stats as stats
prob = 1 - stats.binom.cdf(6,10,0.5)
print("The probability of getting more than 6 heads from 10 fair coin flips is:", prob)