# https://adventofcode.com/2022/day/2
from pathlib import Path

TABLE = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

MOVES = [
    {"rock": "scissors", "paper": "rock", "scissors": "paper"},  # key wins to value
    {"rock": "rock", "paper": "paper", "scissors": "scissors"},  # key draws to value
    {"rock": "paper", "paper": "scissors", "scissors": "rock"},  # key loses to value
]

SCORES = {"rock": 1, "paper": 2, "scissors": 3, "lose": 0, "draw": 3, "win": 6}

filepath = Path(f"input_{Path(__file__).stem}.txt")

total_score = 0
with filepath.open("r") as stream:
    for line in stream:
        line = line.strip("\n")

        score = 0
        opponent_move_str = TABLE.get(line.split(" ")[0])
        desired_result_str = TABLE.get(line.split(" ")[1])

        result_score = SCORES.get(desired_result_str)
        tmp_index = result_score // 3

        needed_move = MOVES[tmp_index].get(opponent_move_str)
        move_score = SCORES.get(needed_move)

        score = result_score + move_score
        total_score += score

        print(
            f"my opponent will use {opponent_move_str} i am supposed to {desired_result_str}"
        )
        print(f"so i must choose {needed_move}")

# solution for part 2
print(total_score)  # in my case 13726
