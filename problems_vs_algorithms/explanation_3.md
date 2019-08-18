### Rearrage Array Elements to Form Max Sum

For this problem, I chose to implement the solution using the QuickSort algorithm.  This approach sorts the elements in descending order, then arranges the elements at even numbered indexes into one integer, and repeats for the elements at the odd numbered indexes.

#### Time Complexity:

The time complexity of this problem is O(nlog(n)) worst case because the QuickSort algorithm recursively splits the array into an upper and lower (log(n)) half until the order is achieved.  The space complexity is O(n) since the array is sorted in place, which maintains the size.


