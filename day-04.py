# https://adventofcode.com/2022/day/4

from pathlib import Path

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path("2022") / Path(filename)

with filepath.open("r") as stream:
    complete_overlap = 0
    overlap = 0
    for line in stream:
        line = line.strip("\n")

        pair = line.split(",")
        low_1, high_1 = tuple(map(int, pair[0].split("-")))
        low_2, high_2 = tuple(map(int, pair[1].split("-")))

        if low_1 >= low_2 and high_1 <= high_2:
            complete_overlap += 1
        elif low_2 >= low_1 and high_2 <= high_1:
            complete_overlap += 1
        elif low_1 >= low_2 and low_1 <= high_2:
            overlap += 1
        elif low_2 >= low_1 and low_2 <= high_1:
            overlap += 1

    overlap += complete_overlap


# solution part 1
print(complete_overlap)  # in my case 573

# solution part 2
print(overlap)  # in my case 294
