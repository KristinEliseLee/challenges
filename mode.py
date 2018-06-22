"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""
    count = {}
    modes = set()
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    most_appearances = 1
    for x in count:
        if count[x] > most_appearances:
            most_appearances = count[x]
    for n in count:
        if count[n] == most_appearances:
            
            modes.add(n)

    return modes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. HOORAY!\n")
