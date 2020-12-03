from functools import reduce

data = open("data.csv", "r")
lines = [x.replace("\n", "") for x in data.readlines()]


def get_tree_count(x, rise, run):

    width = len(lines[0])
    trees = 0
    x = 0
    for line in lines[::rise]:

        if line[x] == "#":
            trees += 1
        x = (x + run) % width
    return trees


product = reduce(
    lambda x, y: x * y,
    [
        get_tree_count(lines, 1, 1),
        get_tree_count(lines, 3, 1),
        get_tree_count(lines, 5, 1),
        get_tree_count(lines, 7, 1),
        get_tree_count(lines, 1, 2),
    ],
)
