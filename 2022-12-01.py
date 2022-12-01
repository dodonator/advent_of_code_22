# https://adventofcode.com/2022/day/1
from pathlib import Path
from typing import List

filename = "2022-12-01_input.txt"
filepath = Path(filename)

elves: List[int] = []

with filepath.open("r") as stream:
    current_total: int = 0  # current calorie total
    elf_counter = 0  # index of the current elf

    for line in stream:
        line = line.strip("\n")

        if line:
            # add value to total
            cal = int(line)
            print(f"elf {elf_counter:>2}: {cal:>10}")
            current_total += int(line)

        else:
            # save total to list
            elves.append(current_total)
            current_total = 0
            elf_counter += 1
    else:
        # add the last total
        elves.append(current_total)

# sort the elves by their calorie total descending
elves.sort(reverse=True)

# answer part 1
print(max(elves))

# answer part 2
print(sum(elves[:3]))
