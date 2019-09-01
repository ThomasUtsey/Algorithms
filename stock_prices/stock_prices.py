import argparse
#!/usr/bin/python
'''You want to write a bot that will automate the task of day-trading for you while you're 
going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 
Write a function `find_max_profit` that receives as input a list of stock prices. 
Your function should return the maximum profit that can be made from a single buy and sell. 
You must buy first before selling; no shorting is allowed here.
For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the 
maximum profit that can be made from a single buy and then sell of these stock prices. 
import argparse
'''


def find_max_profit(prices):
    current_min, max_profit, potential = prices[0], 0, 0
    for i in range(1, len(prices)-1):
        if prices[i] > current_min:
            max_profit = prices[i]
            potential = max_profit - current_min
        if potential > max_profit:
            max_profit = potential - current_min
        if prices[i] < current_min:
            current_min = prices[i]
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
