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

phone_number = '240-877-9220'
my_text = 'Is {} a phone number?'.format(phone_number)

print(my_text)
print(is_phone_number(phone_number))