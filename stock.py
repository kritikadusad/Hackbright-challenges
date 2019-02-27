"""Return maximum profit possible for buying-and-selling a stock.

The `best` function will be given a list of stock prices as they
happened throughout the day::

    best([15, 10, 20, 22, 1, 9])

It should return the maximum possible profit on the stock for that day.
For example, with these prices, our best option would have been to
buy the stock at $10 and sell it at $22. So the profit would be $12::

    >>> best([15, 10, 20, 22, 1, 9])
    12

Best profit: $4 (buy at $1, sell at $5)::

    >>> best([1, 2, 3, 4, 5])
    4

Other tests:

    >>> best([2, 3, 10, 6, 4, 8, 1])
    8

    >>> best([7, 9, 5, 6, 3, 2])
    2

    >>> best([0, 100])
    100

Io profit is possible, so return $0::

    >>> best([5,4 ,3, 2, 1])
    0

    >>> best([100])
    0

    >>> best([100, 0])
    0



"""


def best(prices):
    """"Given a list of prices, return the maximum profit.

    If no profit is possible, return 0.
    """
    min_price = prices[0]
    max_price = prices[0]
    for price in prices[1:]:
        if min_price > price:
            min_price = price
        else:
            break
    for price in prices[1:]:
        if price > max_price:
            max_price = price

    if min_price >= max_price:
        return 0
    if prices.index(min_price) > prices.index(max_price):
        return 0
    return max_price - min_price


if __name__ == '__main__':
    import doctest

    print()
    if doctest.testmod().failed == 0:
        print("\t*** ALL TESTS PASSED; YOU CAN TAKE THAT TO THE BANK!")
    print()
