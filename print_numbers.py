"""
Description: Function to print the numbers from 1-100,
             where multiples of 3 and 5 are replaced with string "ThreeFive",
             multiples of 3 are replaced with "Three" and multiples of 5 are replaced with "Five"
             modulus operation is used to find out if the number is a multiple or not.

author     : Naveen Krishnamurthy
Date       : 11-06-2020
"""

def numbers_print():
    """ Function to print the numbers from 1-100,
        where multiples of 3 and 5 are replaced with string "ThreeFive",
        multiples of 3 are replaced with "Three" and multiples of 5 are replaced with "Five"
    """
    values=[each for each in range(1,101)]
    num_lis = []
    for value in values:
        if value%3 == 0:
            # multiple of 3 and 5
            if value%5 == 0:
                num_lis.append("ThreeFive")
            # multiple of 3 only
            else:
                num_lis.append("Three")

        # multiple of 5 only
        elif value%5 == 0:
            num_lis.append("Five")

        # not multiple of 3 or 5
        else:
            num_lis.append(value)
    return num_lis

num_lis = numbers_print()
print(num_lis)
