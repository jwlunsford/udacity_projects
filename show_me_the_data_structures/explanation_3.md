### Problem 3 - Huffman Node

#### Reasoning:
For this problem, I chose to implement the solution using a custom object called a HuffmanTree().  This object is used to produce a tree using the character frequencies.  This object calculates the frequencies, builds the tree, makes the codes, and decodes the message.  The tree building mechanism uses a native Python list to simulate a heap strucure.  This made it easy to sort the heap using the sort() method on lists, and the minimum values could be popped from the heap as needed.


#### Efficiency:
* Time efficiency - O(n log n) worst case.  The array used as a heap in this code must be sorted each time a new node is inserted.  The array is a native python structure that uses O(n log n) time.  All other functions use O(n) time.
* Space efficiency - O(n) worst case, where n is the number of unique characters in the input data.


