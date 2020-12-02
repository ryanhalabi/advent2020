my_file = open("data_1.csv", "r")
x = [int(x.replace("\n", "")) for x in my_file.readlines()]


def find_n_value(expenses, target=2020, n=3):
    if n == 1 and target in expenses:
        return [target]
    elif n == 1:
        return None
    while expenses:
        x = expenses.pop()
        c = target - x
        if found := find_n_value(expenses[:], target=c, n=n - 1):
            found.append(x)
            return found


two = find_n_value(x.copy(), 2020, 2)
three = find_n_value(x.copy(), 2020, 3)
