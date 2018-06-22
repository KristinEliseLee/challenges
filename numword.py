"""Convert an integer number to the word representation.

We should handle zero:

    >>> num_word(0)
    'zero'

And numbers under a thousand:

    >>> num_word(2)
    'two'

    >>> num_word(-2)
    'negative two'

    >>> num_word(11)
    'eleven'

    >>> num_word(20)
    'twenty'

    >>> num_word(100)
    'one hundred'

    >>> num_word(121)
    'one hundred twenty one'

And numbers over a thousand:

    >>> num_word(1256)
    'one thousand two hundred fifty six'

    >>> num_word(100001)
    'one hundred thousand one'

    >>> num_word(1000000)
    'one million'

And all numbers ranging from -999,999,999,999 to 999,999,999,999 (you
can stop there):

    >>> num_word(-1234567890)  # doctest:+NORMALIZE_WHITESPACE
    'negative one billion two hundred thirty four million
    five hundred sixty seven thousand eight hundred ninety'

    >>> num_word(999999999999)  # doctest:+NORMALIZE_WHITESPACE
    'nine hundred ninety nine billion nine hundred ninety nine million
    nine hundred ninety nine thousand nine hundred ninety nine'

"""


def num_word(num):
    """Convert word to number."""
    general_numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
        "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90
        }

    multiplier_numbers = {"hundred": 100, "thousand": 1000, "million": 1000000,
    "billion": 1000000000
    }
    num = num.split()
    answer = 0

    #find the current multiplier
    def current_multiplier(place, list):
        if i < len(num) - 1:
            for x in range(i + 1, len(num)):
                if num[x] in multiplier_numbers:
                    if num[x] == "hundred" and i < len(num) - 2:
                        for j in range(x + 1, len(num)):
                            if num[j] in multiplier_numbers:
                                return 100 * multiplier_numbers[num[j]]

                    else:
                        return multiplier_numbers[num[x]]
        else:
            return 1

    for c in range(len(num)):
        if num[c] in general_numbers:
            current_number = general_numbers[num[c]] * current_multiplier(c, num)


    if num[1] == "negative":
        answer *= -1

    return answer

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. GREAT JOB!\n")
