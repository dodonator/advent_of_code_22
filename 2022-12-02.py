# https://adventofcode.com/2022/day/2
from pathlib import Path

CHOICES = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

SCORES = {"ROCK": 1, "PAPER": 2, "SCISSOR": 3}

RESULTS = {
    ("ROCK", "ROCK"): 4,
    ("ROCK", "PAPER"): 8,
    ("ROCK", "SCISSORS"): 3,
    ("PAPER", "ROCK"): 1,
    ("PAPER", "PAPER"): 5,
    ("PAPER", "SCISSORS"): 9,
    ("SCISSORS", "ROCK"): 7,
    ("SCISSORS", "PAPER"): 2,
    ("SCISSORS", "SCISSORS"): 6,
}

filepath = Path(f"input_{Path(__file__).stem}.txt")

total_score = 0
with filepath.open("r") as stream:
    for line in stream:
        line = line.strip("\n")

        tmp = line.split(" ")
        enemy_choice = CHOICES.get(tmp[0])
        my_choice = CHOICES.get(tmp[1])

        result = (enemy_choice, my_choice)
        score = RESULTS.get(result)
        total_score += score
        print(result, score)

# solution part 1
print(total_score)
