# https://adventofcode.com/2022/day/7

from pathlib import Path

filename = f"input_{Path(__file__).stem}.txt"
filepath = Path("2022") / Path(filename)

content = filepath.read_text()
lines = list(filter(bool, content.split("$ ")))

TOTAL_DISK_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000

cwd = Path()
paths = {}

for line in lines:
    if line.startswith("cd"):
        # get directory name
        directory = line.strip("\n").split(" ")[-1]

        # go to parent
        if directory == "..":
            cwd = cwd.parent

        else:
            cwd = cwd / Path(directory)
            paths[cwd] = 0

    elif line.startswith("ls"):
        names = list(filter(bool, line.split("\n")))
        names.pop(0)

        for entry in names:
            if entry.startswith("dir"):
                _, directory = entry.split(" ")

            else:
                size, file = entry.split(" ")
                size = int(size)
                file = cwd / Path(file)

                for p in file.parents:
                    paths[p] += size

    print(f"{cwd=}")
    print()

# add up large files
total_size = 0
for path, size in paths.items():
    if size < 100_000:
        total_size += size

# solution part one
print(f"solution part one: {total_size}")

free_space = TOTAL_DISK_SPACE - paths.get(Path("/"))
needed_space = UPDATE_SIZE - free_space

possible_dirs_to_delete = filter(lambda size: size > needed_space, paths.values())

# solution part two
print(f"solution part two: {min(possible_dirs_to_delete)}")
