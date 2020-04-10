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


def is_palindrome(str):
    return str == reverse_string(str)


print(is_palindrome('radar'))
print(is_palindrome('rootbeer'))
