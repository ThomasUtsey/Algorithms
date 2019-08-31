#!/usr/bin/python

import sys

# create a dictionairy to store data to make calls faster
cache = {}
pocket = 0


def making_change(amount, denominations):
    # check if amount is in cache and return it
    if amount in cache:
        return cache[amount]
# check that amount is 0 and return 1
    if (amount == 0):
        return 1
# handle negative values or empty denom
    if (amount < 0 or denominations == []):
        return 0
# recursion to check handle amount
    else:
        pocket = making_change(
            amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])
        # cache[amount] = pocket

        return(pocket)

#     if sum(pocket) == amount:
#       # if amount is = to the pocket value return pocket as value
#         yield pocket
#     else:
#         for d in making_change(amount, denominations[:]):
#             yield d
#         for d in making_change(amount, denominations[1:], pocket):
#             yield d


# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
