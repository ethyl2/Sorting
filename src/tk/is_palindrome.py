import string
from reverse_string import reverse_string

"""
Write a function that takes a string as a parameter 
and returns True if the string is a palindrome, False otherwise. 

For bonus points palindromes can also be phrases, 
but you need to remove the spaces and punctuation before checking. 
For example: madam i’m adam is a palindrome. 

Other palindromes include:
radar
kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
"""


def is_palindrome(mystr):
    # Take out spaces and punctuation
    mystr = mystr.replace(' ', '')
    mystr = mystr.translate(str.maketrans('', '', string.punctuation))
    # Make everything lowercase
    mystr = mystr.lower()
    print(mystr)
    return mystr == reverse_string(mystr)


print(is_palindrome('radar'))
print(is_palindrome('rootbeer'))
print(is_palindrome('Reviled did I live, said I, as evil I did deliver'))
print(is_palindrome("Go hang a salami; I'm a lasagna hog."))
print(is_palindrome("Live not on evil"))
print(is_palindrome('Able was I ere I saw Elba'))
print(is_palindrome('Wassamassaw'))
print(is_palindrome("Go hang a salami 2; I'm a lasagna hog. 2"))
print(is_palindrome("2Go hang a salami; I'm a lasagna hog.2"))
