# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

import time

word_numbers = {
    0: ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    1: ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'],
    2: ['', 'one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred',
        'seven-hundred', 'eight-hundred', 'nine-hundred'],
    3: ['', 'one-thousand'],
}


replacements = {
    'ten one': 'eleven',
    'ten two': 'twelve',
    'ten three': 'thirteen',
    'ten four': 'fourteen',
    'ten five': 'fifteen',
    'ten six': 'sixteen',
    'ten seven': 'seventeen',
    'ten eight': 'eighteen',
    'ten nine': 'nineteen'
}


# Converts the given integer into a human readable string
def convert(n):
    if n > 1000:
        raise NotImplementedError()

    result = ''

    for index, c in enumerate(reversed(str(n))):
        word = word_numbers[index][int(c)]
        if word != '':
            conjunction = ' and ' if index == 2 else ' '

            if result != '':
                result = word + conjunction + result
            else:
                result = word

    # Post processing for special exceptions
    for r in replacements.keys():
        if r in result:
            result = result.replace(r, replacements[r])

    return result


def word_length(word):

    count = 0

    for i in word:
        if i != ' ' and i != '-':
            count += 1

    return count


if __name__ == '__main__':
    t0 = time.time()

    result = 0

    for i in xrange(1, 1001):
        word = convert(i)
        result += word_length(word)

        print word

    runtime = time.time() - t0
    print 'Result = {}'.format(result)
    print 'Runtime = {}'.format(runtime)
