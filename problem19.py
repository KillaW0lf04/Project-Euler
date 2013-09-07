# You are given the following information, but you may prefer to do some research for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import time

from utils import is_leap_year

# Count the number of days between 1 Jan 1901 and 31 Dec 2000 and divide by 7? (Need to cater for the last year somehow)

dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Days per month
dpm = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

assert dpm[months.index('Jan')] == 31
assert dpm[months.index('Feb')] == (28, 29)
assert dpm[months.index('Mar')] == 31
assert dpm[months.index('Apr')] == 30
assert dpm[months.index('May')] == 31
assert dpm[months.index('Jun')] == 30
assert dpm[months.index('Jul')] == 31
assert dpm[months.index('Aug')] == 31
assert dpm[months.index('Sep')] == 30
assert dpm[months.index('Oct')] == 31
assert dpm[months.index('Nov')] == 30
assert dpm[months.index('Dec')] == 31

# For testing, use http://www.dayoftheweek.org/

if __name__ == '__main__':
    t0 = time.time()

    # Jan 1st 1900 was a Monday
    index = dow.index('Tuesday')

    # Feb 1st 1900 was a Thursday
    assert dow[31 % 7] == 'Thursday'

    # Jan 1st 1901 was a Tuesday
    assert dow[365 % 7] == 'Tuesday'

    result = 0

    for year in xrange(1901, 2001):
        for i, month in enumerate(months):

            if dow[index % 7] == 'Sunday':
                print '{} 1st {} was on a Sunday'.format(month, year)
                result += 1

            # Move forward one month

            # Special case for february
            if i == months.index('Feb'):
                index += dpm[i][1] if is_leap_year(year) else dpm[i][0]
            else:
                index += dpm[i]

    print 'Jan 01 2001 was a {}'.format(dow[index % 7])

    runtime = time.time() - t0

    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
