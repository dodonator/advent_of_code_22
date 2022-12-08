# https://adventofcode.com/2022/day/5

from pathlib import Path
from parse import parse

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path("2022") / Path(filename)

with filepath.open("r") as stream:
    content = stream.read()
    # split content on empty line
    start_configuration = content.split("\n\n")[0].split("\n")
    movement_commands = content.split("\n\n")[1].split("\n")

# last line of conf contains the header
header_row = start_configuration.pop()
# parse the header row
header = list(filter(bool, header_row.strip("\n").split(" ")))

# flip the table
start_configuration.reverse()

# create an table for the indices
index_table = {}
for number in header:
    index_table[number] = header_row.index(number)

stacks = {number: [] for number in header}

for row in start_configuration:
    for number in header:
        index = index_table[number]
        value = row[index]
        if value == " ":
            continue
        stacks[number].insert(0, value)

for cmd in movement_commands:
    # parse movement commands
    result = parse("move {} from {} to {}", cmd)
    if result is None:
        break

    size, source, target = result
    size = int(size)

    # get the crates from source stack
    crates = stacks[source][:size]

    # flip crate order to emulate moving crates one at a time
    crates.reverse()  # comment this out for part two

    # delete crates from source stack
    del stacks[source][:size]

    # append crates on top of target stack
    stacks[target] = crates + stacks[target]

# solution
print("solution: ")
print("".join((stack[0] for _, stack in stacks.items())))
