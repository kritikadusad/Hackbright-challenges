"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""

from string import ascii_lowercase


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    letters_in_sentence = set()
    for letter in sentence:
        if letter.isalpha():
            letters_in_sentence.add(letter.lower())
    alphabet = set()
    for char in ascii_lowercase:
        alphabet.add(char)

    return len(letters_in_sentence) == len(alphabet)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
