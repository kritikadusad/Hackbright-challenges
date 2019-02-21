"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    len_data = len(bio_data)
    start_results = {}
    end_results = {}
    for i in range(len_data):
        start = bio_data[i][1]
        end = bio_data[i][2]
        if start not in start_results:
            start_results[start] = 0
        for i in range(len_data):
            if start in range(bio_data[i][1], bio_data[i][2]):
                start_results[start] += 1
        if end not in end_results:
            end_results[end] = 0
        for i in range(len_data):
            if end in range(bio_data[i][1], bio_data[i][2]):
                end_results[end] += 1

    max_start = max(start_results.values())
    start_date = []
    for key in start_results:
        if start_results[key] == max_start:
            start_date.append(key)

    max_end = max(end_results.values())
    end_date = []
    for key in end_results:
        if end_results[key] == max_end:
            end_date.append(key)

    return (min(start_date), min(end_date))


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
