# postcode_validator_numbers_generator
UK postcodes validation and formatting, multiples of 3 and 5 number generation.

Problem statement:
1) Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”. 

2) Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.

print_numbers.py  ----- solution for 1

UK_postcode.py  ----- solution for 2

unit_test.py  ----- unit test for functionality of 1 and 2

print_numbers.py
  function(s)
    - numbers_print() : To print the number in the pattern as per 1.

UK_postcode.py
  function(s)
   - postcode_valid(): To check the validity of the postcode as per, 
                       https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    
   - postcode_data() : To retrieve UK postcode data from http://postcodes.io/
   
   - outward_data()  : To retrieve out outward postcode from the data returned from API endpoint (http://postcodes.io/)
   
   - inward_data()   : To retrieve out inward postcode from the data returned from API endpoint (http://postcodes.io/)
   
   - show_details()  : Priniting out the details of the postcode supplied.

python3 project

Cloning the Repository
   - git clone https://github.com/nkrishx/postcode_validator_numbers_generator.git
Install the requirements
  - pip install -r requirements.txt
  
Run unit test
  - python -m unittest unit_test.py

Import functions from individual files for using them
  - eg: from UK_postcode import show_details()
      - show_details("DN55 1PT")
  - eg: from UK_postcode import *
   
