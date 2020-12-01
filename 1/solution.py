def num_finder(x):
    x = set(x)
    for y in x:
        complement = 2020 - y
        if complement in x:
            return complement * y
x = [1721, 979, 366, 299, 675, 1456]
y = num_finder(x)