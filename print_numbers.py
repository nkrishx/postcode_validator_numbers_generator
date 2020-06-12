def numbers_print():
    """ Function to print the numbers from 1-100,
        where multiples of 3 and 5 are replaced with string "ThreeFive",
        multiples of 3 are replaced with "Three" and multiples of 5 are replaced with "Five"
    """
    values=[each for each in range(1,101)]
    for value in values:
        if value%3 == 0:
            # multiple of 3 and 5
            if value%5 == 0:
                print("ThreeFive")
            # multiple of 3 only
            else:
                print("Three")

        # multiple of 5 only
        elif value%5 == 0:
            print("Five")

        # not multiple of 3 or 5
        else:
            print ("{}" .format(value))

numbers_print()
