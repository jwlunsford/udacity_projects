### Max and Min in an Unsorted Array

#### Design:
For this problem, I chose to implement this using a for loop.  By setting the inital min and max values to the first element in the loop I could traverse each element and update the min and max values accordingly.

#### Time Complexity:
Time complexity is O(n) worst, average and best case.  The function calls each element in the list once and only once, regardless of how many values are in the list, or their sign.

#### Space Complexity:
Space complexity is also O(n), where n is the size of the array passed into the function.  Auxillary space is constant O(1), because no additonal space is required with respect to input size.
