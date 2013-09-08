# The Fibonacci sequence is defined by the recurrence relation:
#
# F[n] = F[n-1] + F[n-2], where F[1] = 1 and F[2] = 1.
# Hence the first 12 terms will be:
#
# F[1] = 1
# F[2] = 1
# F[3] = 2
# F[4] = 3
# F[5] = 5
# F[6] = 8
# F[7] = 13
# F[8] = 21
# F[9] = 34
# F[10] = 55
# F[11] = 89
# F[12] = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import time


if __name__ == '__main__':
    t0 = time.time()

    # Do not use fibonacci from utils for performance (We can reuse results here)

    buffer = [0, 1]  # Circular buffer for holding previous 2 terms

    i = 2
    while True:
        value = buffer[0] + buffer[1]

        if len(str(value)) == 1000:
            break

        buffer[i % 2] = value
        i += 1

    runtime = time.time() - t0

    print 'Result = {}'.format(i)
    print 'Runtime = {}'.format(runtime)
