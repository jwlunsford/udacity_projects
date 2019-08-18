### Dutch National Flag Problem

For this problem, I chose to implement the solution using a variant of the QuickSort algorithm.  This approach uses a three-way-partition (bottom=0, middle=1, and top=2).  The values are sorted in place to the appropriate location, 0's to the left, 1's in the middle, and 2's at the top of the array.  This algorithm is robust to repeated elements.

#### Time Complexity:

The time complexity of this problem is O(n) worst case because the algorithm works in a single traversal of the array.  The space complexity is also O(n) since the array is sorted in place, which maintains the size.


