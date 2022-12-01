import requests
from pathlib import Path
import datetime


def load_session_key(filename):
    filepath = Path(filename)
    with filepath.open("r") as stream:
        session_key = stream.read()
    return session_key


def download_input_data(year: int, day: int) -> Path:

    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    output_file = f"input_{year}-12-{day:0>2}.txt"

    output_path = Path(output_file)
    if output_path.exists():
        return output_path

    session_key = load_session_key("session_key.txt")
    req = requests.get(input_url, cookies={"session": session_key})

    if not output_path.exists():
        output_path.touch()

    text = req.text

    with output_path.open("w") as stream:
        stream.write(text)

    return output_path


if __name__ == "__main__":
    today = datetime.date.today()
    year, day = today.year, today.day
    out = download_input_data(year, day)
    print(out)
