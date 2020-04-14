# The helper function merges 2 sorted arrays
import random


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    # starting at beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    index = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr[index] = arrA[0]
            # print(merged_arr)
            del arrA[0]
        elif arrB[0] < arrA[0]:
            merged_arr[index] = arrB[0]
            # print(merged_arr)
            del arrB[0]
        index += 1

    while len(arrA) > 0:
        merged_arr[index] = arrA[0]
        del arrA[0]
        index += 1

    while len(arrB) > 0:
        merged_arr[index] = arrB[0]
        del arrB[0]
        index += 1

    return merged_arr


# print(merge([1, 4, 5], [2, 6, 7]))
# print(merge([8, 9, 13, 15], [2, 16, 17, 20]))

"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled

"""


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        return merge(merge_sort(arr[: len(arr)//2]), merge_sort(arr[len(arr)//2:]))

# print(merge_sort([2, 1, 3, 6, 0, 13]))


# STRETCH: implement an in-place merge sort algorithm

"""
"What do you mean by “in-place”? A standard merge sort requires you to allocate a buffer equal in 
length to the input being sorted. For example, if you wish to sort an array with 1000 elements, 
it is necessary to allocate an additional scratch array with 1000 elements as a space for merging 
elements before copying them back to the input array. This is why merge sort has O(n) space complexity.

An in-place sorting algorithm doesn’t require allocating any additional memory for sorting. 
Several algorithms meet this requirement, including insertion sort and heap sort which have O(1) space 
complexity. However, in-place merge sort has O(log n) space complexity. 
This is because, like quick sort, it is a recursive function which requires pushing elements onto the stack.
"""


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


def quick_sort(arr):
    # Ave time complexity: O(n log n) Worst case: 0(n^2)
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


def shuff(n=10):
    arr = list(range(n))
    random.shuffle(arr)
    return arr


def quick_sort_in_place(arr, low, high):
    print(arr)
    # if len(arr) <= 1:
    #    return arr
    print('low:', low, 'high: ', high)
    if low < high:
        pivot = arr[0]
        pivot_ind = 0
        for i in range(1, len(arr)):
            if arr[i] <= pivot:
                # 2 swaps: 1. pivot (arr[0]) and arr[i]
                arr[pivot_ind], arr[i] = arr[i], arr[pivot_ind]
                pivot_ind = i
                # 2. arr[i] (which contains the pivot value) and arr[where the pivot value should be]
                while arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    pivot_ind = i-1
        quick_sort_in_place(arr, 0, pivot_ind - 1)
        quick_sort_in_place(arr, pivot_ind + 1, high)
    else:
        return arr


my_arr = [6, 4, 5, 2, 1, 3]
print(quick_sort_in_place(my_arr, 0, len(my_arr) - 1))
print(my_arr)

# print(quick_sort(shuff()))
