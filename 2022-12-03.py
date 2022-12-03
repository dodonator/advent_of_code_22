# https://adventofcode.com/2022/day/3

from pathlib import Path
from string import ascii_uppercase, ascii_lowercase
from more_itertools import grouper

chars = "#" + ascii_lowercase + ascii_uppercase

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path(filename)


def part_one():
    priority_sum = 0
    with filepath.open("r") as stream:
        for line in stream:
            line = line.strip("\n")
            # get number of items
            item_number = len(line)
            # split line at midpoint
            midpoint = item_number // 2
            first, second = set(line[:midpoint]), set(line[midpoint:])
            # get intersection of compartments
            common = set.intersection(first, second).pop()
            priority = chars.index(common)
            print(priority)
            # add up priorities
            priority_sum += priority

    # solution part 1
    return priority_sum  # in my case 7826


def part_two():
    with filepath.open("r") as stream:
        lines = (line.strip("\n") for line in stream.readlines())

    groups = grouper(lines, 3)
    for g in groups:
        pass
