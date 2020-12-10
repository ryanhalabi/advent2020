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







# dynamic programming solution

has_gold_map = {x: 0 for x in rules.keys()}
def check_has_gold(color, has_gold_map=has_gold_map):

    print("\n",color)
    # contains gold
    children = [a[0] for a in rules[color]]
    if "shiny gold" in children:
        print(f"{color} found direct gold")
        has_gold_map[color] = 1
        return True

    # contains nothing
    if not children:
        has_gold_map[color] = -1
        return False

    for child in children:
        
        # check map
        child_has_gold = has_gold_map[child]
        print(child, child_has_gold)

        # if map has gold, done
        if child_has_gold == 1:
            print(f"{color} found gold in {child}")
            has_gold_map[color] = 1
            return True

        # if map has no gold, do nothing
        if child_has_gold == -1:
            continue

        # if unknown, explore
        if child_has_gold == 0:
            print("exploring children")
            child_has_gold = check_has_gold(child, has_gold_map)

            if child_has_gold:
                has_gold_map[color] = 1
                print(f"{color} found gold in {child}")
                return True

    has_gold_map[color] = -1
    return False


for color in rules.keys():
    check_has_gold(color)

print(has_gold_map)


# zechs solution


from collections import defaultdict
import re
​
def eventually_contains(target_bag, input_string):
    rule_map = parse_input(input_string)
    contained_in_map = build_contained_in_map(rule_map)
    found = set()
    checked = set()
    recursively_check_contains(target_bag, contained_in_map, found, checked)
    return found
​
def count_contained(bag, input_string):
    rule_map = parse_input(input_string)
    return recursively_count_bags(bag, rule_map, {})
​
​
​
def parse_input(input_string):
    rule_map = {}
    for rule_string in input_string.split("\n"):
        bag, rules = parse_rule(rule_string)
        rule_map[bag] = rules
    return rule_map
​
def parse_rule(rule_string):
    bag, rules_string = rule_string.split(" bags contain", 1)
    return (bag, re.findall(" (\d+) ([\w ]+) bag", rules_string))
​
​
def build_contained_in_map(rule_map):
    """converts a mapping of bags and what they contain -- rulemap: bag => [(#, bag),]
    to a mapping of bags and what they are contianed in -- contains_map: bag => set(bag,)
    """
    contained_in_map = defaultdict(set)
    for parent_bag, children in rule_map.items():
        for _, child_bag in children:
            contained_in_map[child_bag].add(parent_bag)
    return contained_in_map
​
def recursively_check_contains(target_bag, contained_in_map, found, checked):
    """mutates found"""
    if target_bag in checked or target_bag not in contained_in_map:
        # already checked (or) no bags hold this bag
        return
    checked.add(target_bag)
    for bag in contained_in_map[target_bag]:
        found.add(bag)
        if bag not in checked:
            recursively_check_contains(bag, contained_in_map, found, checked)
​
def recursively_count_bags(target_bag, rule_map, known_counts):
    if target_bag not in rule_map:
        return 0
    total_count = 0
    for num, bag in rule_map[target_bag]:
        if bag not in known_counts:
            known_counts[bag] = recursively_count_bags(bag, rule_map, known_counts)
        total_count += int(num) * (known_counts[bag] + 1) # counting itself
    return total_count