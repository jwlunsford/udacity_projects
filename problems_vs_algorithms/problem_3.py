# REARRANGE ARRAY ELEMENTS

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    try:
        # catch error when list has a negative number
        if any(n < 0 for n in input_list):
            raise ValueError

        arrX = list()       # these will temporarily hold the values
        arrY = list()
        output = list()
        n = len(input_list)

        # Check for single list entry
        if n == 1:
            # only one value in input list, return it
            return [input_list[0]]

        # First we must sort the values in descending order
        desc_list = sort_all(input_list, 0, n-1)

        # Then we need to add each value at an even index to the X list,
        # and each value at an odd index to the Y list
        arrX = input_list[::2]
        arrY = input_list[1::2]

        # join values into a single integer
        valueX_asString = [str(x) for x in arrX ]
        valueX_asInt = int(''.join(valueX_asString))
        output.append(valueX_asInt)

        valueY_asString = [str(y) for y in arrY]
        valueY_asInt = int(''.join(valueY_asString))
        output.append(valueY_asInt)

        return output

    except ValueError:
        return print(f'Error: Input list cannot include a negative value.')


# SORT USING QUICK-SORT ALGORITHM
def pivot_and_arrange_desc(items, begin_index, end_index):
    '''This sorts in descending order.  Choose a pivot value from the array
       and move all values smaller above it, and all values larger below it.
    '''
    right_index = end_index
    pivot_index = begin_index
    pivot_value = items[pivot_index]  # start with the last value as the pivot

    while (pivot_index != right_index):

        # select the next item
        item = items[right_index]

        # item is less move right pointer down the array to the next item
        if item <= pivot_value:
            right_index -= 1
            continue

        items[right_index] = items[pivot_index + 1]
        items[pivot_index + 1] = pivot_value
        items[pivot_index] = item
        pivot_index += 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    '''recursive function to sort an array.'''
    if end_index <= begin_index:
        return

    # first pass move pivot to the middle, smaller values to right, larger to left
    pivot_index = pivot_and_arrange_desc(items, begin_index, end_index)

    # recursively pick a new pivot in upper and lower ends
    sort_all(items, begin_index, pivot_index - 1)   # lower end
    sort_all(items, pivot_index + 1, end_index)     # upper end


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# TEST CASES

test_function([[1, 2, 3, 4, 5], [542, 31]])                     # Simple Case -- Returns Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])                 # Simple Case -- Returns Pass
test_function([[2, 2, 2, 2, 2, 2], [222, 222]])                 # Edge Case -- Returns Pass
test_function([[9], [9]])                                       # Edge Case - Returns Pass

rearrange_digits([-1, 2, 3, 4, 5])                              # Error Case list contains a negative value
                                                                # - Returns Error Message