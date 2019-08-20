def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]  # randomly set min and max to the first value in the list
    max = ints[0]

    for i in ints:
        if i > max:
            max = i

        if i < min:
            min = i

    return min, max




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")    # should return Pass

m = [1, 12, 3, 9, 8, 4, 2, 20, 14]
print("Pass" if ((1, 20) == get_min_max(m)) else "Fail")    # should return Pass


n = [-5, -20, -10, -3, -2, -12]  # all negative values
print("Pass" if ((-20, -2) == get_min_max(n)) else "Fail")   # should return Pass

n = [1, 1, 1, 1, 1, 1]  # all same values
print("Pass" if ((1, 1) == get_min_max(n)) else "Fail")   # should return Pass

