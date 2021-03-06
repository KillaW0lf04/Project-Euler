# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#            3
#           7 4
#          2 4 6
#         8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

problem = '    \n\
               75\n\
              95 64\n\
             17 47 82\n\
            18 35 87 10\n\
           20 04 82 47 65\n\
          19 01 23 75 03 34\n\
         88 02 77 73 07 63 67\n\
        99 65 04 28 06 16 70 92\n\
       41 41 26 56 83 40 80 70 33\n\
      41 48 72 33 47 32 37 16 94 29\n\
     53 71 44 65 25 43 91 52 97 51 14\n\
    70 11 33 28 77 73 17 78 39 68 17 57\n\
   91 71 52 38 17 14 91 43 58 50 27 29 48\n\
  63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

import time


# Uses a brute forced / exhaustive search to determine the longest path
def exhaustive_search(triangle_list, i=0, j=0):

    if i >= len(triangle_list) or j >= len(triangle_list[i]):
        return 0

    value = int(triangle_list[i][j])

    # An item at row i, column j is related to
    # item at row i+1, column j and
    # item at row i+1, column j+1
    path1 = exhaustive_search(triangle_list, i+1, j)
    path2 = exhaustive_search(triangle_list, i+1, j+1)

    return value + max(path1, path2)


if __name__ == '__main__':
    t0 = time.time()

    sections = problem.split('\n')
    rows = []

    for i in sections:
        rows.append([col for col in i.split(' ') if col != ''])

    del rows[0]
    result = exhaustive_search(rows)

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
