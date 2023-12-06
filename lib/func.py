import requests as r
from env import SESSION_ID


def fetch(day):
    url = f"https://adventofcode.com/2023/day/{day}/input"
    cookies = dict(session=SESSION_ID)
    response = r.get(url, cookies=cookies)

    hasTerminalNewLine = response.text[-1] == "\n"
    print(f"New Line: {hasTerminalNewLine}")
    return response.text if not hasTerminalNewLine else response.text[:-1]


def reduce(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + reduce(arr[1:])
