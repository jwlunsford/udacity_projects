# Search in a Rotated Sorted Array

def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    n = len(input_list)
    pivot = seek_pivot(input_list, 0, n-1)
    if pivot == -1:
        return -1

    if input_list[pivot] == target:
        return pivot
    if target >= input_list[0]:    # search the left side of the array
        return binary_search(input_list, 0, pivot-1, target)

    # default case, search right side of the array
    return binary_search(input_list, pivot+1, n-1 , target)


def binary_search(array, low, high, target):
    """searches for a value in an array using binary search.
       Returns -1 if target is not found.
    """

    # high cannot be less than low
    if low > high:
        return -1

    # choosing to do an iterative approach here versus a recursive
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < target:    # check upper end
            low = mid + 1
        elif array[mid] > target:  # check lower end
            high = mid - 1
        else:
            return mid
    return -1


def seek_pivot(input, low, high):
    """ Return the pivot index in the pivoted array.  Pivot will be the
        value for which the next element is smaller.
    """
    if high < low:
        return -1
    if high == low:
        return low

    mid = (low + high) // 2  # find the floor of the midpoint

    # check possible cases...
    # case where pivot is the middle value
    if mid < high and input[mid] > input[mid + 1]:
        return mid
    # case where pivot is one less than the middle value
    if mid > low and input[mid] < input[mid - 1]:
        return mid - 1
    # pivot is in lower end of the array, increment down and search again
    if input[low] >= input[mid]:
        return seek_pivot(input, low, mid-1)

    # pivot is in the upper end of the array, increment up and search again
    return seek_pivot(input, mid + 1, high)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])