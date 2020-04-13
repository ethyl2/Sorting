# TO-DO: Complete the selection_sort() function below
"""
Start with current index = 0

For all indices EXCEPT the last index:

a. Loop through elements on right-hand-side of current index and find the smallest element

b. Swap the element at current index with the smallest element found in above loop

"""


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
"""
Loop through your array
Compare each element to its neighbor
If elements in wrong position (relative to each other, swap them)
If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

"""


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
"""
Look into Counting Sort.

How is this algorithm different from other iterative sorting algorithms?

It "sorts the elements of an array by counting the number of occurrences 
of each unique element in the array. The count is stored in an auxiliary 
array and the sorting is done by mapping the count as an index of the auxiliary array."

What are the advantages/disadvantages to this type of sorting algorithm?
Take a look a the pseudocode for this algorithm and try implementing it in Python.

1. Find out the maximum element (let it be max) from the given array.

2. Initialize an array of length max+1 with all elements 0. 
This array is used for storing the count of the elements in the array.

3. Store the count of each element at their respective index in count array

4. Store cumulative sum of the elements of the count array. That is,
modify the count array such that each element at each index 
  stores the sum of previous counts. 

5. Find the index of each element of the original array in count array. 
This gives the cumulative count. Place the element at the index calculated.

6. After placing each element at its correct position, decrease its count by one.

"""


def count_sort(arr, maximum=-1):
    # Find the largest element in the array
    # Assuming we can't use the built-in max()?
    if len(arr) == 0:
        return arr
    max = arr[0]
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        if num > max:
            max = num

    # Initialize count array with all zeros
    count_arr = [0] * (max + 1)

    # Loop through arr and find the total count of each unique element
    # Store the count at the corresponding index in count array
    for num in arr:
        count_arr[num] += 1
    # print(count_arr)

    # modify the count array such that each element at each index stores the sum of previous counts.
    my_sum = 0
    for i in range(len(count_arr)):
        my_sum += count_arr[i]
        count_arr[i] = my_sum
    # print(count_arr)

    # Loop thru array.
    # For each value x in arr, find count_arr[x]. Take that value - 1 to find index to put x in the return_array.
    # Then decrease the value of count_arr[x] by 1.
    return_arr = [0] * len(arr)

    for num in arr:
        # print(num)
        index = count_arr[num] - 1
        return_arr[index] = num
        count_arr[num] -= 1

    print(return_arr)
    return return_arr


# count_sort([3, 3, 1])
count_sort([4, 6, 3, 1, 3, 9, 2])

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
# print(insertion_sort(my_arr_14))
