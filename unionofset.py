set_1 = {'A','B','C','D','E'}
set_2 = {'B','D','X','Y','Z'}
union = set_1.union(set_2)
total_guest = list(union)
print("Total guests to be invited to party is:", len(total_guest))
print("Guest list is:", total_guest)