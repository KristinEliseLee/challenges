"""How many days are there in a month?

Given a string with a month and a year (separated by a space),
returns the number of days in that month.

For example::

    >>> for i in range(1, 13):
    ...     date = str(i) + " 2016"
    ...     print "%s has %s days." % (date, days_in_month(date))
    1 2016 has 31 days.
    2 2016 has 29 days.
    3 2016 has 31 days.
    4 2016 has 30 days.
    5 2016 has 31 days.
    6 2016 has 30 days.
    7 2016 has 31 days.
    8 2016 has 31 days.
    9 2016 has 30 days.
    10 2016 has 31 days.
    11 2016 has 30 days.
    12 2016 has 31 days.

    >>> days_in_month("02 2015")
    28
"""


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?"""
    date_list = date.split()
    month_list_31 = ["01", "03", "05", "07", "08", "10", "12"]
    if date_list[1] in month_list_31:
        return 31
    elif date_list[1] != "02":
        return 30
    else:
        if is_leap_year(int(date_list[2])):
            return 29
        else:
            return 28


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASSED. W00T!\n")