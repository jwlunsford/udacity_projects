### HTTP Router Using a TRIE

#### Design:
For this problem, I created the RouteTrie and Route classes, allowing for a handler url passed as a parameter with leading or trailing slashes.  For example, either '/path1/path2/path3/' or '/path1/path2/path3' will work.  The function for splitting the path uses the Python split() function to split the string at each occurance of '/', returning a list.  For time sake, I chose not implement the Not Found Handler portion.  For a complete path, the Trie will store and return the handler.  This is a mock handler, returned only as a string.

#### Time Complexity:
The time complexity for add_handler() and lookup() operations are O(n) worst case.  The split_path() function ensures that only nodes in the path are accessed in each of these operations, and not all nodes contained in the Trie.

#### Space Complexity:
Space complexity for the insert(), find() and split_path() functions are all O(n) linear time.  The split_path function takes one string variable as input and creates a list of multiple variables as output.  Insert() and Find() take the resulting list of values from split_path(), and then perform linear searches on that list.  Thus they are O(n) linear as well.  Auxillary space is O(1) since additional space is not required by these functions.

