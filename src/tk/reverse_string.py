"""Write a function that takes a string as a parameter 
and returns a new string that is the reverse of the old string.
"""


def reverse_string(str):
    if len(str) == 1:
        return str[0]
    else:
        return str[-1] + reverse_string(str[: -1])


print(reverse_string('cow'))
# print(reverse_string('123456789'))
