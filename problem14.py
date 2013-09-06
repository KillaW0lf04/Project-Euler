# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem - http://en.wikipedia.org/wiki/Collatz_conjecture),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time


# Generate the next item in the sequence
def gen_next(n):

    if n % 2 == 0:
        # Even
        return n/2
    else:
        # Odd
        return (3 * n) + 1


if __name__ == '__main__':
    t0 = time.time()

    cache = {}
    max_count = 0
    result = 0

    for i in xrange(1, 1000000):

        if i % 100000 == 0:
            print i

        step = i
        count = 0

        while step != 1:
            count += 1
            step = gen_next(step)

            if step in cache:
                count += cache[step]
                break

        # Cache previous values
        # We will use these during the generation
        # of further sequences
        cache[i] = count

        if count > max_count:
            max_count = count
            result = i

    runtime = time.time() - t0

    print 'Result = {} ({})'.format(result, max_count)
    print 'Runtime = {}'.format(runtime)
