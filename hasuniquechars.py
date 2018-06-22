"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""


def has_unique_chars(word):
    """Does word contains any unique characters? Returns True or False"""

    for i in range(len(word)-1):
        if word[i] in word[i+1:]:
            return False
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. AWESOME!\n")
