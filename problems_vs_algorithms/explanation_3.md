### Rearrage Array Elements to Form Max Sum

#### Design:
For this problem, I chose to implement the solution using the QuickSort algorithm.  This approach sorts the elements in descending order, then arranges the elements at even numbered indexes into one integer, and repeats for the elements at the odd numbered indexes.

#### Time Complexity:
The time complexity of this problem is O(nlog(n)) worst case because the QuickSort algorithm recursively splits the array into an upper and lower (log(n)) half until the order is achieved.

#### Space Complexity:
The Quicksort alogrithm implemented uses a recursive call to sort the upper and lower half of the array each time.  Therefore, the auxillary space required is O(log(n)) space for the additional stacks.




