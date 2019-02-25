"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):

    sorted_lst = merge_sort_helper(lst)
    assert(len(lst) == len(sorted_lst))
    for i in range(len(sorted_lst)):
        lst[i] = sorted_lst[i]


def merge_sort_helper(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""
    # print(lst)

    len_lst = len(lst)
    if len_lst < 2:
        return lst
    else:
        i = int(len_lst / 2)

        left = merge_sort_helper(lst[:i])
        right = merge_sort_helper(lst[i:])

        return merge(left, right)


def merge(left, right):
    # l=[3], r=[10]
    # l=[3, 8], r=[5, 9, 10,]
    #  l=[1, 3, 10], r=[2, 4, 6]
    # l = [1, 3, 10], r = [2]

    left_index = 0
    right_index = 0
    results = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            results.append(right[right_index])
            right_index += 1
        else:
            results.append(left[left_index])
            left_index += 1
    if left_index < len(left):
        results.extend(left[left_index:])
    else:
        results.extend(right[right_index:])

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AWESOME WORK!\n")
