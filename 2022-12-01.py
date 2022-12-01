# https://adventofcode.com/2022/day/1
from pathlib import Path

filename = "2022-12-01_input.txt"
filepath = Path(filename)

elves = []

with filepath.open("r") as stream:
    calories = 0
    elf_counter = 0

    for line in stream:
        line = line.strip("\n")
        if line:
            cal = int(line)
            print(f"elf {elf_counter:>2}: {cal:>10}")
            calories += int(line)
        else:
            elves.append(calories)
            print(f"elf {elf_counter:>2} sum: {calories:>6}")
            print("#" * 20)
            calories = 0
            elf_counter += 1
    else:
        elves.append(calories)
        print(f"elf {elf_counter:>2} sum: {calories:>6}")
        print("#" * 20)

# answer part 1
print(max(elves))

elves.sort(reverse=True)
# print(elves)
# print(elves[:3])
print(sum(elves[:3]))
