"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next

    def __repr__(self):
        return "<Node data=%s has prev=%s and next=%s>" % (
            self.data, self.previous.data, self.next.data)

    @classmethod
    def circular_linkedlist(cls, n):
        first = cls(1)
        previous = first
        for i in range(2, n + 1):
            person = Node(i)
            previous.next = person
            person.previous = previous
            previous = person

        person.next = first
        first.previous = person

        return first


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""
    start = Node.circular_linkedlist(num_people)
    while start.next != start:
        for i in range(kill_every - 1):
            start = start.next
        current = start.next
        current.previous = start.previous
        start.previous.next = current
        start = current
    return start.data


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
