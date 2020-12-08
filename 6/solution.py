import re
from functools import reduce

data = open("data.csv", "r")
data = data.read()
data = data.replace("\n\n", "||||").replace("\n", " ").replace("||||", "\n").split("\n")
data = [ x.split(" ") for x in data]



group_counts_1 = 0
for group in data:
     group_counts_1 += len(set(reduce(lambda x,y: x+y,group)))



from collections import Counter

group_counts_2 = 0
for group in data:
    group_size = len(group)
    counts = Counter(reduce(lambda x,y: x+y,group))
    all_counts = [x for (x,y) in counts.items() if y == group_size]

    group_counts_2 += len(all_counts)