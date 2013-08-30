# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from utils import factorise

if __name__ == '__main__':
    value = 600851475143

    factors = factorise(value)

    print max(factors)

