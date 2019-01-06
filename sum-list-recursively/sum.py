"""Sum a list of integers using recursion.

Given a list of numbers, return the sum. Do not use the built in 'sum' method.

For example::

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

The sum of an empty list is zero::

    >>> sum_list([])
    0

"""


def sum_list(nums):
    """Using recursion, return the sum of numbers in a list."""
    if len(nums) == 0:
        return 0

    else:
        sum_nums = nums[0] + sum_list(nums[1:])
        return sum_nums


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
