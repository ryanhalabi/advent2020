import re

data = open("data.csv", "r")
lines = [x.replace("\n", "") for x in data.readlines()]

def check_valid_old(password, char, char_min, char_max):
    char_count = password.count(char)
    return char_min <= char_count <= char_max

def check_valid_new(password, char, position_1, position_2):
    return (password[position_1 - 1] == char) ^ (password[position_2 - 1] == char)


old_count, new_count = 0, 0
for line in lines:

    line = re.search(r"(\d+)-(\d+) (\w): (\w+)", line)
    char_min = int(line.group(1))
    char_max = int(line.group(2))
    char = line.group(3)
    password = line.group(4)

    if check_valid_old(password, char, char_min, char_max):
        old_count += 1

    if check_valid_new(password, char, char_min, char_max):
        new_count += 1



