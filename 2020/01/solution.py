"""
1/ Find the two entries that sum to 2020; what do you get if you multiply them
together?
2/ What is the product of the three entries that sum to 2020?
"""

from itertools import combinations
from functools import reduce
from operator import mul

"""
Version 1 - longer solution
"""

with open('input.txt', mode='r') as file:
    puzzle_input1 = [int(num) for num in file.read().strip().splitlines()]


def find1(num):
    for mix in combinations(puzzle_input1, num):
        if sum(mix) == 2020:
            print(mix)
            return reduce(mul, mix)  # python3.8 -> math.prod(mix)


"""
Version 2 - one line solution
"""

puzzle_input2 = list(map(int, open('input.txt').read().strip().splitlines()))


def find2(num):
    return reduce(mul, [mix for mix in combinations(
        puzzle_input2, num) if sum(mix) == 2020][0])


print(find1(2))
print(find1(3))
print(find2(2))
print(find2(3))
