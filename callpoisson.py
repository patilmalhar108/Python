#The average number of calls bewtween 9am and 10am is 15 calls. What is the probabilty of observing
#more than 20 calls? Also find the probability of observing between 17-21 calls
import scipy.stats as stats
prob = 1 - stats.poisson.cdf(20,15)
print("The probability of observing more than 20 calls is:", prob)
prob2 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)
print("The probability of observing between 17-21 calls is:", prob2)