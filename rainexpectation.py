#We expect it to rain 10 times in next 30 days. Calculate the probability of exactly 6 days of rain.
#Also calculate the probability of 12-14 days of rain
import scipy.stats as stats
prob = stats.poisson.pmf(6,10)
print("The probability of exactly 6 days of rain is:", prob)
prob2 = stats.poisson.pmf(12,10) + stats.poisson.pmf(13,10) + stats.poisson.pmf(14,10)
print("The probability of 12-14 days of rain:", prob2)