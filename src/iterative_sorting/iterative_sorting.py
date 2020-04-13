# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    had_swaps = True
    while had_swaps == True:
        had_swaps = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                had_swaps = True
    return arr

# Here's another implementation from the debugger presentation, just for reference:


def bubble_sort2(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


"""
Insertion Sort:

Separate the first element from the rest of the array. Think about it as a sorted list of one element.

For all other indices, beginning with [1]:

a. Copy the item at that index into a temp variable

b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted

Shift items over to the right as you iterate
c. When the correct index is found, copy temp into this position

"""


def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr


my_arr_14 = [6, 14, 13, 7, 14]
print(insertion_sort(my_arr_14))
