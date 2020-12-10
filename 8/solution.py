import re
import numpy as np

data = open("data.csv", "r")
data = data.read()
data = data.split("\n")

data = [list(re.findall(r"([\w]+) ([+-][\d]+)", x)[0]) for x in data]


def process_lines(data):
    line_visits = {k: 0 for k in range(len(data))}

    accum = 0
    index = 0
    while True:
        print(index)

        if line_visits[index] == 1:
            print("found a loop")
            break
        line_visits[index] += 1

        op_type = data[index][0]
        op_amount = int(data[index][1])

        if op_type == "acc":
            accum += op_amount
            index += 1

        elif op_type == "jmp":
            index += op_amount

        elif op_type == "nop":
            index += 1

        if index == len(data) - 1:
            print("end of the line")
            return False, accum, line_visits
    return True, accum, line_visits


is_loop, accum, line_visits = process_lines(data)


possible_errors = [
    k
    for k, v in line_visits.items()
    if v == 1 and ((data[k][0] == "jmp") or (data[k][0] == "nop"))
]


for i in possible_errors:

    possible_fix = list(data)

    fix_value = list(possible_fix[i])
    fix_value[0] = "jmp" if fix_value[0] == "nop" else "nop"

    possible_fix[i] = fix_value

    is_loop, accum, line_visits = process_lines(possible_fix)

    print(f"{i} fix is a loop {is_loop}")

    if not is_loop:
        print("{i} fixed it!")
        break