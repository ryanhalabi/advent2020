import re
import json

necessary_items = sorted(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
)


def check_1(line):
    present_needed_keys = sorted([x for x in line.keys() if x in necessary_items])
    return necessary_items == present_needed_keys


def check_2(line):
    if check_1(line):

        byr = 1920 <= int(line["byr"]) <= 2002
        if not byr:
            return False

        iyr = 2010 <= int(line["iyr"]) <= 2020
        if not iyr:
            return False

        eyr = 2020 <= int(line["eyr"]) <= 2030
        if not eyr:
            return False

        hgt = re.search(r"(\d+)(cm|in)", line["hgt"])
        if hgt:
            if hgt.group(2) == "in":
                hgt = 59 <= int(hgt.group(1)) <= 76
            elif hgt.group(2) == "cm":
                hgt = 150 <= int(hgt.group(1)) <= 193
        if not hgt:
            return False

        hcl = bool(re.search("#[0-9a-f]{6}$", line["hcl"]))
        if not hcl:
            return False

        ecl = line["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if not ecl:
            return False

        pid = bool(re.search("^[0-9]{9}$", line["pid"]))
        if not pid:
            return False

        return True

    return False


data = open("data.csv", "r")
data = data.read()
data = data.replace("\n\n", "||||").replace("\n", " ").replace("||||", "\n").split("\n")
data = [re.findall(r"(\w+):([^ ]+)", line) for line in data]
data = [{k: v for (k, v) in line} for line in data]


valids_1, valids_2 = [], []
for line in data:

    if check_1(line):
        valids_1.append(sorted(line.keys()))
    if check_2(line):
        valids_2.append(line)

print(len(valids_1))
print(len(valids_2))