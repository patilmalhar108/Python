def prob_a_b(a,b,all_possible_outcomes):
    prob_a = len(a)/len(all_possible_outcomes)
    prob_b = len(b)/len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_inter = len(inter)/len(all_possible_outcomes)
    return (prob_a + prob_b - prob_inter) 

even = {2,4,6} 
greater_than_2 = {3,4,5,6}
all_possible_rolls = {1,2,3,4,5,6}

print("Probability of getting an even number or a number > 2")
print(prob_a_b(even, greater_than_2, all_possible_rolls))