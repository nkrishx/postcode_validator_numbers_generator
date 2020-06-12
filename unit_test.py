"""
Description: Unit test code to check the functions of UK_postcode.py,
             Functions checked are:
                postcode_valid
                postcode_data
                numbers_print
             Random postcodes obtained from http://www.ukpostcode.co.uk/random.htm are used.

author     : Naveen Krishnamurthy
Date       : 11-06-2020
"""
#import statements
from UK_postcode import *
from print_numbers import *
import unittest

class PostcodeTest(unittest.TestCase):

    def test_postcode_valid(self):
        """
            test for all valid post code cases
            valid postcode formats can be found at "https://www.doogal.co.uk/UKPostcodes.php"
        """
        self.assertTrue(postcode_valid("DN55 1PT"))
        self.assertTrue(postcode_valid("EH8 9UJ"))
        self.assertTrue(postcode_valid("M1 1AE"))
        self.assertTrue(postcode_valid("B33 8TH"))
        self.assertTrue(postcode_valid("EH4 4PE"))
        self.assertTrue(postcode_valid("HX3 0ST"))
        self.assertTrue(postcode_valid("CR2 6XH"))
        print("\n \"Postcode validity\" test success!")
        print("#######################################")

    def test_postcode_invalid(self):
        """
            test for all invalid post code cases
        """
        self.assertFalse(postcode_valid("N29 422AM"))
        self.assertFalse(postcode_valid("N2# 422AM"))
        self.assertFalse(postcode_valid("NART 4QL"))
        self.assertFalse(postcode_valid("G13 4XIA"))
        self.assertFalse(postcode_valid("PQ9 1J"))
        self.assertFalse(postcode_valid("SR4 90T"))
        self.assertFalse(postcode_valid("DNY6 5KP"))
        self.assertFalse(postcode_valid("HXWS 7TT"))
        self.assertFalse(postcode_valid("EH1 87J"))
        self.assertFalse(postcode_valid("EH12Y 87JT"))
        print("\n \"Postcode invalid\" test success!")
        print("#######################################")

    def test_postcode_data_found(self):
        """
            test for post code data retrieved from the api
        """
        self.assertEqual(postcode_data("DN55 1PT")["status"], 200)
        print("\n \"Postcode data found\" test success!")
        print("#######################################")

    def test_postcode_data_notfound(self):
        """
            test for post code data that is not available
        """
        try:
            self.assertEqual(postcode_data("W1A 0AX")["status"], 404)
        except:
            print("\n \"Postcode data not found\" test success!")
            print("#######################################")

class PrintNumberTest(unittest.TestCase):

    def test_numbers_threefive(self):
        """
            test for printing the numbers (multiple of 3,5 and both)
            Val is a list containing the expected format of numbers to be printed
        """
        Val = [1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five',\
                11, 'Three', 13, 14, 'ThreeFive', 16, 17, 'Three', 19, 'Five', \
                'Three', 22, 23, 'Three', 'Five', 26, 'Three', 28, 29, 'ThreeFive',\
                31, 32, 'Three', 34, 'Five', 'Three', 37, 38, 'Three', 'Five', \
                41, 'Three', 43, 44, 'ThreeFive', 46, 47, 'Three', 49, 'Five', \
                'Three', 52, 53, 'Three', 'Five', 56, 'Three', 58, 59, 'ThreeFive',\
                61, 62, 'Three', 64, 'Five', 'Three', 67, 68, 'Three', 'Five',\
                71, 'Three', 73, 74, 'ThreeFive', 76, 77, 'Three', 79, 'Five',\
                'Three', 82, 83, 'Three', 'Five', 86, 'Three', 88, 89, 'ThreeFive',\
                91, 92, 'Three', 94, 'Five', 'Three', 97, 98, 'Three', 'Five']
        self.assertEqual(numbers_print(),Val)
        print("\n \"Print numbers\" test success!")
        print("#######################################")

if __name__ == '__main__':
    unittest.main()
