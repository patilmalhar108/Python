set_1 = {'A','B','C','D','E'}
set_2 = {'B','D','V','X','Y','Z'}
common = set_1.intersection(set_2)
total_guests = list(common)
print("Total number of guests are:", len(total_guests))
print("Guests coming to party are:", total_guests)