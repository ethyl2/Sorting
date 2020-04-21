"""
Write a recursive search function that receives as 
input an array of integers and a target integer value. 
This function should return True if the target element exists in the array, and 
False otherwise.
"""


def rec_search(arr, target):
    if len(arr) == 1:
        return arr[0] == target
    return rec_search(arr[:len(arr)//2], target) + rec_search(arr[len(arr)//2:], target)


print(rec_search([10, 2, 34, 0, 1, 32, 15], 122))  # 0
print(rec_search([10, 2, 34, 0, 1, 32, 15], 34))  # 1
