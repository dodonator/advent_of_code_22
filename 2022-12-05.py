# https://adventofcode.com/2022/day/5

from pathlib import Path
from parse import parse

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path("2022") / Path(filename)

with filepath.open("r") as stream:
    content = stream.read()
    # split content on newline
    conf = content.split("\n\n")[0].split("\n")
    moves = content.split("\n\n")[1].split("\n")

# last line of conf contains the header
header_row = conf.pop()
# parse the header row
header = list(filter(bool, header_row.strip("\n").split(" ")))

# flip the table
conf.reverse()

# create an table for the indices
index_table = {}
for number in header:
    index_table[number] = header_row.index(number)

stacks = {number: [] for number in header}

for row in conf:
    for number in header:
        index = index_table[number]
        value = row[index]
        if value == " ":
            continue
        stacks[number].insert(0, value)

print(stacks)

# parse movement commands
# move 5 from 4 to 9

for cmd in moves:
    result = parse("move {} from {} to {}", cmd)
    if result is None:
        break
    size, source, target = result
    size = int(size)

    current = stacks[source][:size]
    current.reverse()
    del stacks[source][:size]
    stacks[target] = current + stacks[target]

# solution part one
# get first crate of each stack
print("".join((stack[0] for _, stack in stacks.items())))
