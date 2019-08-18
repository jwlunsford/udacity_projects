# Square root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # return f'{number} is not a valid number. Please try again.'
    try:
        # let's raise an error if the parameter is not an integer
        if not isinstance(number, int):
            raise TypeError

        if number == 0 or number == 1:
            return number

        # will search between begin and end
        begin = 0
        end = number
        ret_val = 0

        while begin <= end:
            mid = (begin + end) // 2   # calculate the mid value
            mid_squared = mid * mid    # square mid

            # iterate until a solution is found
            if mid_squared == number:
                return mid

            if mid_squared < number:
                # search the upper half
                begin = mid + 1      # increment by one
                ret_val = mid        # need this to deal with cases where number is not an even square
            else:
                # search the lower half
                end = mid - 1

        return ret_val

    except TypeError:
        return f'Error: {number} is not a valid integer. Please try again.'


# TEST CASES
print(sqrt(16))          # should return 4

print(sqrt(1))           # square of 1 is 1

print(sqrt(0))           # square of 0 is 0

print(sqrt(33))          # not an even square, should return 5

print(sqrt('x'))         # case where input is not a number, should return Error.

print(sqrt(5.54))        # case where input is not an integer, should return Error.