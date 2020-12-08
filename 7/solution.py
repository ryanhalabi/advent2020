import re
import numpy as np

data = open("data.csv", "r")
data = data.read()
data = data.split("\n")

rules = {}
for line in data:
    line_re = re.search(r"(.+) bags contain[s]* (.+).", line)

    key = line_re.group(1)

    contains = line_re.group(2)
    if contains == "no other bags":
        rules[key] = []
    else:
        contains = contains.split(", ")
        contains = [re.search(r"([\d]+) (.+) bag", x) for x in contains]
        contains = [(x.group(2), x.group(1)) for x in contains]
        rules[key] = contains

# create matrix
mat = np.zeros([len(rules), len(rules)])
keys = sorted(rules.keys())

for color, insides in rules.items():
    i = keys.index(color)
    for inside_color, amount in insides:
        j = keys.index(inside_color)
        # if i == 0:
        #     print(color, i , ":", inside_color, j)
        mat[j, i] = amount


# How many bag colors can eventually contain at least one shiny gold bag?
shiny_gold_index = keys.index("shiny gold")
contains_gold = 0
for i in range(mat.shape[0]):

    i_vector = np.zeros(mat.shape[0])
    i_vector[i] = 1

    if i == shiny_gold_index:
        continue

    while True:
        if i_vector[shiny_gold_index] > 0:
            contains_gold += 1
            break
        if i_vector.sum() == 0:
            break

        i_vector = np.matmul(mat, i_vector)


print(contains_gold)


# How many individual bags are required inside your single shiny gold bag?

i_vector = np.zeros(mat.shape[0])
i_vector[shiny_gold_index] = 1

bag_sum = 0
while True:
    i_vector = np.matmul(mat, i_vector)

    bag_sum += i_vector.sum()
    if i_vector.sum() == 0:
        break

