import re
import json

data = open("data.csv", "r")
data = data.read()
data = data.split("\n")

# O(N)
ids = []
for line in data:
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    aisle = int(line[7:].replace("R", "1").replace("L", "0"), 2)
    id = row * 8 + aisle
    ids.append(id)

# O(N)
answer_1 = max(ids)

# O(N)
answer_2 = [x for x in range(min(ids), max(ids)+1) if x not in ids]
