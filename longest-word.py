"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return length of longest word in list of words."""
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word

    return len(longest)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")
