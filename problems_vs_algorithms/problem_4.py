# DUTCH NATIONAL FLAG PROBLEM

def sort_012(array):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       array(list): List to be sorted
    """
    mid = 1
    i = 0
    j = 0
    n = len(array) - 1

    # iteratively sort the list
    while j <= n:
        if array[j] < mid:
            # swap a[i] and a[j], then increment position i and j
            elem_i = array[i]  # get the elements
            elem_j = array[j]
            array[i] = elem_j  # swap them
            array[j] = elem_i
            i += 1
            j += 1
        elif array[j] > mid:
            elem_n = array[n]  # get the elements
            elem_j = array[j]
            array[n] = elem_j  # swap them
            array[j] = elem_n
            n -= 1
        else:
            # j is equal to mid, increment position j
            j += 1

    return array

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# TEST CASES
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])    # should return Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])  # should return Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])  # should return Pass

test_function([0])  # should return Pass
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0])   # should return Pass
