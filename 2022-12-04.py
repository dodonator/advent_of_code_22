# https://adventofcode.com/2022/day/4

from pathlib import Path

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path("2022") / Path(filename)

with filepath.open("r") as stream:
    overlap_counter = 0
    for line in stream:
        line = line.strip("\n")

        pair = line.split(",")
        low_1, high_1 = tuple(map(int, pair[0].split("-")))
        low_2, high_2 = tuple(map(int, pair[1].split("-")))

        if low_1 >= low_2 and high_1 <= high_2:
            overlap_counter += 1
        elif low_2 >= low_1 and high_2 <= high_1:
            overlap_counter += 1
        else:
            pass
# solution part 1
print(overlap_counter)  # in my case 573
