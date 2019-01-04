"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    # check if word is palindrome
    letters_in_word = {}
    for letter in word:
        if letter not in letters_in_word:
            letters_in_word[letter] = 0
        letters_in_word[letter] += 1

    count_letters = letters_in_word.values()

    if len(word) % 2 == 0:
        for count in count_letters:
            if count % 2 != 0:
                return False

    else:
        odd = 0
        for count in count_letters:
            if count % 2 != 0:
                odd += 1
            if odd > 1:
                return False
    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
