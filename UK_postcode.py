"""
Description: Code for formatting and validating UK postcodes as per,
              https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom
              Postcode and Geolocation information retrieved from http://postcodes.io/
              API endpoints, methods and documentation available at http://postcodes.io/

author    : Naveen Krishnamurthy
Date      : 11-06-2020

"""

import sys
import re
import json
import requests
from geopy.geocoders import Nominatim

def postcode_valid(postcode):
    """
        Splits the supplied postcode randomly generated from https://www.ukpostcode.co.uk/random.htm
        based on the space in the middle to get the outward and inward postcode.
        Uses regular expression on both parts to check if valid.
        Valid post code patterns are defined in https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        The postcodes are alphanumeric, and are variable in length: ranging from six to eight characters (including a space).
    """

    if len(postcode) >= 6 and len(postcode) <= 8:
        try:
            outward = postcode.split(" ")[0]
            inward = postcode.split(" ")[1]
        except:
            return False
    else:
        return False

    if re.match("^[A-PR-UWYZ]{1}(([0-9]{1,2}|[0-9][A-HJKS-UW])|\
([A-HK-Y]{1}([0-9]{1,2}|[0-9][A-Z])))$", outward) is None :
        return False
    if re.match("^[0-9][ABD-HJLNP-UW-Z]{2}$", inward) is None:
        return False
    return True

def postcode_data(postcode, extra_arg=None):
    """
        Sends requests to postcode api (http://postcodes.io/) for getting the data.
        Postcodes.io is free,opensource and based soley on Open Data
        Collects the data in json format.
        If post code is not found ,is not in use or if a request execption is raised, program exits.
        A status '200' indicates succesful request response cycle.
    """
    try:
        url = requests.get('https://api.postcodes.io/postcodes/' + postcode)
        data_postcode = json.loads(url.text)
        if data_postcode["status"] != 200:
            print("\nPost code not found or the post code may not be in use!")
            sys.exit(1)
        else:
            return data_postcode
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

def outward_code(postcode):
    """
        Returns the outward code of the supplied postcode
    """
    if postcode_valid(postcode):
        data_postcode = postcode_data(postcode)
        outwardcode = data_postcode["result"]["outcode"]
        return outwardcode

def inward_code(postcode):
    """
        Returns the inward code of the supplied postcode
    """
    if postcode_valid(postcode):
        data_postcode = postcode_data(postcode)
        inwardcode = data_postcode["result"]["incode"]
        return inwardcode

def show_details(postcode):
    """
        This is to show the information retrieved from the API request,
        To API retuens cordinate (latitude and longitude) values,
        To get the address from the cordinates python geopy is made use of,
        To get the longitude and latitude we will use the Nominatium which requires no API key.
    """
    uk_postcode_str = "https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom"
    print("Supplied Postcode : \"{}\"" .format(postcode.upper()))
    if postcode_valid(postcode):
        data_postcode = postcode_data(postcode)
        result = data_postcode["result"]
        geolocator = Nominatim()
        location = geolocator.reverse(str(result["latitude"]) + "," + str(result["longitude"]))
        print("Valid Postcode: {}".format(str(postcode_valid(postcode))))
        print("Outward Code: {}".format(outward_code(postcode)))
        print("Inward Code: {}".format(inward_code(postcode)))
        print("\nAddress: \n{}".format(location.address))
        print("\nParish: {}\n".format(result["parish"]))
        print("Longitude: {} \nLatitude: {}\n".format(str(result["longitude"]), str(result["latitude"])))
    else:
        print("{} is not a valid postcode".format(postcode))
        print("Please visit {}".format(uk_postcode_str))
