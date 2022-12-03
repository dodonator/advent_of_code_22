# https://adventofcode.com/2022/day/3

from pathlib import Path
from string import ascii_uppercase, ascii_lowercase

chars = "#" + ascii_lowercase + ascii_uppercase

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path(filename)

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
print(priority_sum)  # in my case 7826
