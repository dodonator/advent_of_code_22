# https://adventofcode.com/2022/day/7

from pathlib import Path

filename = f"input_{Path(__file__).stem}.txt"
# filename = f"test_{Path(__file__).stem}.txt"
filepath = Path("2022") / Path(filename)

content = filepath.read_text()
lines = list(filter(bool, content.split("$ ")))

cwd = Path()
paths = {}

for line in lines:
    if line.startswith("cd"):
        directory = line.strip("\n").split(" ")[-1]

        if directory == "..":
            cwd = cwd.parent

        else:
            cwd = cwd / Path(directory)
            paths[cwd] = 0

        print(f"{directory=}")

    elif line.startswith("ls"):
        names = list(filter(bool, line.split("\n")))
        names.pop(0)

        for entry in names:
            if entry.startswith("dir"):
                _, directory = entry.split(" ")
                print(f"listed dir {directory}")

            else:
                size, file = entry.split(" ")
                size = int(size)
                file = cwd / Path(file)

                for p in file.parents:
                    paths[p] += size

                print(f"added {size} bytes to path {cwd} from file {file}")

    print(f"{cwd=}")
    print()

total_size = 0
for path, size in paths.items():
    if size < 100_000:
        print(path, size)
        total_size += size

# solution
print(total_size)
