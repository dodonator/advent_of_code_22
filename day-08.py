# https://adventofcode.com/2022/day/8

from pathlib import Path
from typing import Iterator

aoc_folder = Path.cwd()
input_file = "input_day-08.txt"
test_file = "test_day-08.txt"

filepath = aoc_folder / Path("2022") / Path(input_file)
# filepath = aoc_folder / Path("2022") / Path(test_file)

content = filepath.read_text()
lines = content.split("\n")
lines = list(filter(bool, lines))  # this line should delete blank lines

grid = [list(line) for line in lines]
width = len(grid[0])
height = len(grid)


def left(x, y):
    return [grid[y][i] for i in range(x)]


def right(x, y):
    return [grid[y][i] for i in range(x + 1, width)]


def up(x, y):
    return [grid[i][x] for i in range(y)]


def down(x, y):
    return [grid[i][x] for i in range(y + 1, height)]


visible_counter = 0
for y, row in enumerate(grid):
    for x, value in enumerate(row):
        visible = False

        if x == 0 or x == width - 1:
            # east and west border are always visible
            visible = True
        elif y == 0 or y == height - 1:
            # north and south border are always visible
            visible = True
        elif max(up(x, y)) < value:
            visible = True
        elif max(down(x, y)) < value:
            visible = True
        elif max(left(x, y)) < value:
            visible = True
        elif max(right(x, y)) < value:
            visible = True

        if visible:
            visible_counter += 1

# solution for part one
print(f"number of visible trees: {visible_counter}")
