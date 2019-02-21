"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    word_dict = {}
    for word in wordlist:
        sorted_word = "".join(sorted(word))

        if sorted_word not in word_dict:
            word_dict[sorted_word] = list()
            word_dict[sorted_word].append(word)

        else:
            word_dict[sorted_word].append(word)
    max_len = 0
    max_anagrams = ""
    for word in word_dict:
        if len(word_dict[word]) > max_len:
            max_len = len(word_dict[word])
            max_anagrams = word_dict[word][0]
    return max_anagrams


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
