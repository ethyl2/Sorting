"""
Print out each element of the following array on a separate line:
['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible 
before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""


def print_lines(arr):
    # Loop through the array
    for line in arr:
        print(str(line), type(line))
    # Print each line
    return True


my_arr = ['Joe', 2, 'Ted', 4.98, 14, 'Sam',
          'void *', '42', 'float', 'pointers', 5006]
print_lines(my_arr)
