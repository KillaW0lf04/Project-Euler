# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import time


if __name__ == '__main__':
    t0 = time.time()

    value = str(2**1000)

    result = 0
    for i in value:
        result += int(i)

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
