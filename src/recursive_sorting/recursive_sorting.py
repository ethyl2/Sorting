# TO-DO: complete the helper function below to merge 2 sorted arrays
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
# TO-DO: implement the Merge Sort function below USING RECURSION
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
