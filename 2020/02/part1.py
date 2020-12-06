"""
1/ How many passwords are valid according to these policies?

For example:
1-3 a: abcde  # valid
1-3 b: cdefg  # invalid
2-9 c: ccccccccc  # valid
"""

from re import match
from operator import add
from functools import reduce

"""
Version 1 - longer solution
"""

with open('input.txt', mode='r') as file:
    puzzle_input1 = [line for line in file.read().strip().splitlines()]

number_of_valid_passwords1 = 0

for example in puzzle_input1:
    text = match(r"^(\d+)-(\d+)\s(\w):\s(.+)$", example)
    min, max, char, passw = text.groups()
    if passw.count(char) >= int(min) and passw.count(char) <= int(max):
        number_of_valid_passwords1 += 1

print(number_of_valid_passwords1)

"""
Version 2 - one line solution
"""


def check_validity(line):
    min, max, char, passw = match(r"^(\d+)-(\d+)\s(\w):\s(.+)$", line).groups()
    return 1 if int(min) <= passw.count(char) <= int(max) else 0


number_of_valid_passwords2 = reduce(add, list(
    map(check_validity, open('input.txt').read().strip().splitlines())))

print(number_of_valid_passwords2)
