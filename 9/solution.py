import re
import numpy as np

data = open("data.csv", "r")
data = data.read()
data = [int(x) for x in data.split("\n")]


def is_sum(target, options):
    while options:
        x = options.pop()
        y = target - x
        if y in options:
            return True
    return False

def analyze_list(data, preamble):
    for i in range(preamble, len(data)):
        x = data[i]
        if not is_sum(x, data[i - preamble : i]):
            return x

invalid_num = analyze_list(data, 25)


def continguous_numbers(target, data):

    left, right = 0, 2
    contig_sum = sum(data[left:right])

    while left < len(data):
        if contig_sum == target:
            return left, right
        elif contig_sum < target:
            contig_sum += data[right]
            right += 1
        elif (contig_sum > target) and (left + 2 != right):
            contig_sum -= data[left]
            left += 1
        elif left + 2 == right:
            contig_sum += data[right]
            right += 1


contig_range = continguous_numbers(invalid_num, data)
data_range = data[contig_range[0] : contig_range[1]]

min(data_range) + max(data_range)