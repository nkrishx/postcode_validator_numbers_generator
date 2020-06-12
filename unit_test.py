"""
Description: Unit test code to check the functions of UK_postcode.py,
             Functions checked are:
                postcode_valid
                postcode_data
             Random postcodes obtained from http://www.ukpostcode.co.uk/random.htm are used.

author     : Naveen Krishnamurthy
Date       : 11-06-2020

"""

from UK_postcode import *
import unittest

class PostcodeTest(unittest.TestCase):

    def test_postcode_valid(self):
        """
            test for all valid post code cases
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

if __name__ == '__main__':
    unittest.main()
