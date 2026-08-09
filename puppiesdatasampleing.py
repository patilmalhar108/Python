import numpy as np
np.random.seed(42)
puppies = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
p = puppies.mean()
print("Mean is =", p)
print("Standered Deviation =", puppies.std())
print("Variance is =", puppies.var())

np.random.choice(puppies, size = (1,5), replace = True)
np.random.choice(puppies, size = (1,5), replace = True).mean()
print("\nSampeling distribution with size 5")
sample_proportion = []
for i in range(10000):
    sample = np.random.choice(puppies, 5, replace = True)
    sample_proportion.append(sample.mean())

sample_proportion = np.array(sample_proportion)

sm = sample_proportion.mean()
print("Mean is =", sample_proportion.mean())
print("Standered Deviation is =", sample_proportion.std())
print("Variance is =", sample_proportion.var())

print("\nSampeling distribution with size 20")
sample_proportion = []
for i in range(10000):
    sample = np.random.choice(puppies, 20, replace = True)
    sample_proportion.append(sample.mean())

sample_proportion = np.array(sample_proportion)

sm2 = sample_proportion.mean()
print("Mean is =", sample_proportion.mean())
print("Standered Deviation is =", sample_proportion.std())
print("Variance is =", sample_proportion.var())