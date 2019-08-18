### Search in a Rotated Sorted Array

For this problem, I chose to implement the solution using a Binary Search.  The algorithm finds the pivot value index where the array is rotated.  It then calls Binary Search on one of the two sub-arrays (left or right).  The Binary Search routine can be implemented using an iterative or recursive approach.  I chose to use the iterative approach beacuase it more clearly shows the logic in the comparisons.


#### Time Complexity:

The time complexity of this problem is O(log(n)) worst case because the algorithm searches for a value by splitting the array into two nearly equal parts, then iteratively searching for the target value.  The space complexity is also O(n) since the array is searched in place.
