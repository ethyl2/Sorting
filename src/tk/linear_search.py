"""
Try writing a Python function to perform a linear search on a set of data.

"""
costumes = ['batman', 'viking', 'banana', 'unicorn', 'minion']
target = 'unicorn'


def linear_search(arr, target):
    index = 0
    for item in arr:
        if target == item:
            print('found it')
            return index
        else:
            print('not it')
            index += 1
    return -1


print(linear_search(costumes, target))
