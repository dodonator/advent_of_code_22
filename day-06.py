# https://adventofcode.com/2022/day/6

from pathlib import Path

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path("2022") / Path(filename)

with filepath.open("r") as stream:
    buffer = stream.read()

packet_start = 0
message_start = 0

for i in range(len(buffer)):
    packet = buffer[i : i + 4]
    message = buffer[i : i + 14]

    if len(set(packet)) == 4 and not packet_start:
        packet_start = i + 4

    if len(set(message)) == 14 and not message_start:
        message_start = i + 14

    if packet_start and message_start:
        break

# solution
print(packet_start)  # part one
print(message_start)  # part two
