# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
# the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time


# This can also be performed with the 'permutations' function in itertools
# Produces a list of the lexicographic permutations
def permute(list):
    if len(list) == 1:
        return [list[0]]

    if len(list) == 2:
        if int(list[0]) > int(list[1]):
            return [list[1] + list[0], list[0] + list[1]]
        else:
            return [list[0] + list[1], list[1] + list[0]]

    result = []

    for item in sorted(list):
        internal = permute([i for i in list if i != item])

        result.extend([item + i for i in internal])

    return result


if __name__ == '__main__':
    assert permute(['0', '1', '2']) == ['012', '021', '102', '120', '201', '210']

    t0 = time.time()

    results = permute(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    runtime = time.time() - t0

    print 'Result = {}'.format(results[999999])
    print 'Runtime = {}'.format(runtime)
