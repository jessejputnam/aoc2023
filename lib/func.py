import requests as r
import math
from env import SESSION_ID


def fetch(day):
    url = f"https://adventofcode.com/2023/day/{day}/input"
    cookies = dict(session=SESSION_ID)
    response = r.get(url, cookies=cookies)

    hasTerminalNewLine = response.text[-1] == "\n"

    return response.text if not hasTerminalNewLine else response.text[:-1]


def addArrItems(arr):
    output = 0
    for num in arr:
        output += num
    return output


def getDivisors(num):
    divs = []

    sqrt = math.sqrt(num)
    for i in range(math.floor(sqrt), 0, -1):
        if num % i == 0:
            divs.append(int(num / i))
            if not i == sqrt:
                divs.insert(0, i)
    return divs


def gcd(a, b):
    a_div = getDivisors(a)
    b_div = getDivisors(b)

    gcd = 1
    for num in a_div:
        if (num in b_div) and num > gcd:
            gcd = num

    return gcd


def lcm(a, b):
    return int((a * b) / gcd(a, b))
