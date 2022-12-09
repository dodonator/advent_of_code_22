# https://adventofcode.com/2022/day/1
from pathlib import Path
from typing import Iterator, List
from pprint import pprint as print


def split_list(p_list: List, separator) -> Iterator[List]:
    while separator in p_list:
        ind = p_list.index(separator)
        part = p_list[:ind]
        if part:
            yield part
        p_list = p_list[ind + 1 :]

    if p_list:
        yield p_list


filename = "2022-12-01_input.txt"
filepath = Path(filename)

with filepath.open("r") as stream:
    # strip "\n" from each line
    lines = [line.strip("\n") for line in stream.readlines()]

# convert lines to integer (empty lines become 0)
values = [int(line) if line else 0 for line in lines]

# split list by the empty lines (zero values)
elves = list(sorted((sum(part) for part in split_list(values, 0)), reverse=True))

# part 1
print(elves[0])  # in my case 73211

# part 2
print(sum(elves[:3]))  # in my case 213958
