"""
    A function to validate the syntax of an email address
    Input: an string representing an email
    Output: a boolean value whether it's valid
"""

import re

def checkEmail(email):
    # Check if the email has exactly one '@', at least one '.' in the part after the '@',
    # and at least one character in the parts in between
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False
