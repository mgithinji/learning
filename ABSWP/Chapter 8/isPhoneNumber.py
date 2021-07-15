# Chapter 8: Pattern Matching with Regular Expressions

# In this chapter we will be learning how to perform pattern matching using
# regular expressions (regex). 

"""
Creating a function that checks to see if the input string is a phone number.
This is the brute-force way of performing this check. Later we will show how to
effectively do the same thing using regular expressions.
"""

def is_phone_number(text):
    """
    This function checks the input text to see if it is formatted
    as a phone number. The format xxx-xxx-xxxx.

    :param text: The input string to be checked for phone number format.
    :return: Returns a True if the text is a phone number format, else false.
    """
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8,12):
        if not text[i].isdecimal():
            return False

    return True

# Testing the is_phone_number() method.
cellphone_number = '+1 (240) 877-9220'
office_number = '301-846-4089'
my_text = 'Question: Is {} a phone number?'.format(cellphone_number)

print(my_text)
print(is_phone_number(cellphone_number))

# Pulling the phone number from a message using our is_phone_number() method.
message = 'Call me at {} tomorrow at 5:30pm eastern-time. Thanks! \
    You can also reach me at my office number {}. Goodbye!'.format(cellphone_number, office_number)

def print_all_phone_numbers(message):
    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print('Phone number found: {}'.format(chunk))

print('\nMessage recieved: {}'.format(message))
print('Below is a list of the phone numbers found:')
print_all_phone_numbers(message)
print() # new line

# Performing the check using the Regex module (re).
import re

def is_phone_number_with_regex(text):
    #phone_number_regex = re.compile(r'((\()?\d{3}(\))?-)?\d{3}-\d{4}')
    phone_number_regex = re.compile(r'(\d{3}-\d{3}-\d{4}|\+\d\s\(\d{3}\)\s\d{3}-\d{4})')
    subtext = phone_number_regex.search(text)
    if subtext:
        return True
    else:
        return False

print('Performing check with the regex implementation of the isPhoneNumber() function:')
print(my_text)
print(is_phone_number_with_regex(office_number))

def print_all_phone_numbers_with_regex(message):
    phone_number_regex = re.compile(r'(\d{3}-\d{3}-\d{4}|\+\d\s\(\d{3}\)\s\d{3}-\d{4})')
    phone_numbers = phone_number_regex.findall(message)
    for phone_number in phone_numbers:
        print(phone_number)

print('\nMessage recieved: {}'.format(message))
print('Below is a list of the phone numbers found:')
print_all_phone_numbers_with_regex(message)
print() # new line