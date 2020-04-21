# STRETCH: implement Linear Search

"""
Loop through arr and compare each value to target.
Return index if found.
"""


def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


my_arr_67 = [1, 3, 35, 52, 78, 99]
# print(linear_search(my_arr_67, 52))
# print(linear_search(my_arr_67, 53))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low < high:
        mid = (low + high)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid

    return -1  # not found

# print(binary_search(my_arr_67, 52))
# print(binary_search(my_arr_67, 53))

# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls

    # Base condition. Done searching.
    elif low >= high:
        return -1

    # Base condition. Found target
    elif arr[middle] == target:
        return middle

    elif target < arr[middle]:
        # Ignore arr values higher than middle's
        return binary_search_recursive(arr, target, low, middle)
    else:
        # Ignore arr values smaller than middle's
        return binary_search_recursive(arr, target, middle + 1, high)


# my_arr_67 = [1, 3, 35, 52, 78, 99]
# print(binary_search_recursive(my_arr_67, 35, 0, 6))
# print(binary_search_recursive(my_arr_67, 53, 0, 6))
