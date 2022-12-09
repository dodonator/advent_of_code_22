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

grid = [list(map(int, line)) for line in lines]
width = len(grid[0])
height = len(grid)


def left(x, y):
    return list(reversed([grid[y][i] for i in range(x)]))


def right(x, y):
    return [grid[y][i] for i in range(x + 1, width)]


def up(x, y):
    return list(reversed([grid[i][x] for i in range(y)]))


def down(x, y):
    return [grid[i][x] for i in range(y + 1, height)]


def viewing_distance(x, y, func):
    value = grid[y][x]
    values = func(x, y)
    result = 0
    for val in values:
        if val < value:
            result += 1
        else:
            result += 1
            break

    return result


def scenic_score(x, y):
    west = viewing_distance(x, y, left)
    east = viewing_distance(x, y, right)
    north = viewing_distance(x, y, up)
    south = viewing_distance(x, y, down)
    return west * east * north * south


max_scenic_score = 0
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

        # scenic score
        sc = scenic_score(x, y)

        if sc > max_scenic_score:
            max_scenic_score = sc

# solution for part one
print(f"number of visible trees: {visible_counter}")

# solution for part two
print(f"max scenic score: {max_scenic_score}")
