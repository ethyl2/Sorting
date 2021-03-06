
"""
Try writing a Python function to perform a binary search on a set of data.
"""
nums = [2, 6, 8.9, 99, 125, 888, 78898, 208765]
target2 = 78898
target3 = 6

'''This version assumes that the target IS in the arr'''


def binary_search(arr, target):
    middle = len(nums) // 2
    is_found = False
    while not is_found:
        if nums[middle] == target:
            is_found = True
            print(middle)
        elif nums[middle] < target:
            middle = middle + middle//2
        else:
            middle = middle//2


# binary_search(nums, target2)
# binary_search(nums, target3)


def tk_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high)//2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
    return -1


# print("Time for tk binary search: ")
# print(tk_binary_search(nums, 99))
# print(tk_binary_search(nums, 888))
# print(tk_binary_search(nums, 800))

"""
Can you rewrite the above function so that it uses recursion?
TBD
"""
nums1 = [10, 20, 30]
nums2 = [30, 20, 10]
print(tk_binary_search(nums1, 30))
print(tk_binary_search(nums2, 30))
