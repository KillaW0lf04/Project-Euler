# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

import time

from utils import nCk

# The solution is to calculate the binomial coefficient of
#     ( M + n )
#     (   n   )

if __name__ == '__main__':
    t0 = time.time()

    result = nCk(20 + 20, 20)

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
