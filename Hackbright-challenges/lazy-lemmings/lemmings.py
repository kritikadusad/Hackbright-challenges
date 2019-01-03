"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    furthest_dist = []
    for i in range(num_holes):
        distances = []
        for cafe in cafes:
            distance = abs(cafe - i)
            distances.append(distance)
        best_distance = min(distances)
        furthest_dist.append(best_distance)
    return max(furthest_dist)


# print(furthest(6, [2, 4]))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
