#!/usr/bin/python

import sys

# first turn cache into a dictionary so results of n can be stored to reduce process time of function
# call


def eating_cookies(n, cache={}):
    # Check to see if the value of n is located within the cache dictionary
    if n in cache:
        # return cached n value so no further function call is needed for that specific value of n
        return cache[n]
    # Verify n is not a - number if it is return 0 cause you can eat cookies negative times unless
    # your drunk
    elif n < 0:
        return 0
    # crazy so if the cookie monster has zero cookies he can eat them one way?
    elif n < 1:
        return 1
    # If there only 2 cookies only two ways 1 at a time or all
    elif n == 2:
        return 2
    # if n hasnt found a home yet we need resolve n and determine amount of cookies and store
    #value in dictionairy
    else:
        # here we determine the ways to eat n cookies and store it at the value of key n in
        # dictionary To resolve the numerous ways w resolve that if the value of n is greater
        # 2 we can find the value by (n-1)+(n-2)+(n-3).
        cache[n] = eating_cookies(
            n - 1) + eating_cookies(n-2) + eating_cookies(n-3)
        return cache[n]

    if __name__ == "__main__":
        if len(sys.argv) > 1:
            num_cookies = int(sys.argv[n])
            print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies))
        else:
            print('Usage: eating_cookies.py [num_cookies]')
