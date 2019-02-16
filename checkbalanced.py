"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""


class BinaryNode(object):
  """Node in a binary tree."""

  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def is_balanced(self):
    """Is the tree at this node balanced?"""

    to_visit = [self]
    depths = {self: 0}
    depth_children = []
    while to_visit:
      current = to_visit[0]
      to_visit.pop(0)

      if current.right:
        to_visit.append(current.right)
        depths[current.right] = 1 + depths[current]

      if current.left:
        to_visit.append(current.left)
        depths[current.left] = 1 + depths[current]

      if current.left is None or current.right is None:
        depth_children.append(depths[current])

    return abs(depth_children[0] - depth_children[-1]) <= 1


if __name__ == '__main__':
  import doctest

  if doctest.testmod().failed == 0:
    print("\n*** ALL TEST PASSED! GO GO GO!\n")
