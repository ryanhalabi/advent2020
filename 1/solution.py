# def find_n_value(x, n, target):

#     for a in x:
#         new_target = target - a

#         value = find_n_value(x.pop(a), n-1, new_target)

#         if value:
#             return value * a

#     return None


def two_num_finder(x, value=2020):
    """
    searches list x for 2 values that sum to value and returns their product
    """
    x = set(x)
    for y in x:
        complement = value - y
        if complement in x:
            return complement * y
    return None


def three_num_finder(x, value=2020):
    """
    searches list x for 3 values that sum to value and returns their product
    """
    x = set(x)
    for y in x:
        complement = value - y
        z = two_num_finder(x, value=complement)
        if z:
            return z * y


my_file = open("data_1.csv", "r")
x = [int(x.replace("\n", "")) for x in my_file.readlines()]

y = two_num_finder(x)
z = three_num_finder(x)
