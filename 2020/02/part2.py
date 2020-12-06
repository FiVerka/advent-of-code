"""
2/ Exactly one of these positions must contain the given letter. How many
passwords are valid according to the new interpretation of the policies?

For example:
"1-3 a: abcde" is valid: position 1 contains a and position 3 does not.
"1-3 b: cdefg" is invalid: neither position 1 nor position 3 contains b.
"2-9 c: ccccccccc" is invalid: both position 2 and position 9 contain c.
"""

from re import match
from operator import countOf

"""
Version 1 - longer solution
"""

with open('input.txt', mode='r') as file:
    puzzle_input1 = [line for line in file.read().strip().splitlines()]

number_of_valid_passwords1 = 0

for example in puzzle_input1:
    text = match(r"^(\d+)-(\d+)\s(\w):\s(.+)$", example)
    min, max, char, passw = text.groups()
    if char in passw:
        if (passw[int(min) - 1] == char) != (passw[int(max) - 1] == char):
            number_of_valid_passwords1 += 1


print(number_of_valid_passwords1)

"""
Version 2 - one line solution
"""


def check_validity2(args):
    if args[2] in args[3]:
        return True if (args[3][int(args[0]) - 1] == args[2]) != (
            args[3][int(args[1]) - 1] == args[2]) else None


number_of_valid_passwords2 = countOf([check_validity2(match(
    r"^(\d+)-(\d+)\s(\w):\s(.+)$", example).groups()) for example in open(
        'input.txt').read().strip().splitlines()], True)

print(number_of_valid_passwords2)
