### HTTP Router Using a TRIE

For this problem, I created the RouteTrie and Route classes, allowing for a handler url passed as a parameter with leading or trailing slashes.  For example, either '/path1/path2/path3/' or '/path1/path2/path3' will work.  For time sake, I chose not implement the Not Found Handler portion.  For a complete path, the Trie will store and return the handler.  This is a mock handler, returned only as a string.

#### Time and Space Complexity:

The time, and space, complexity for add_handler() and lookup() operations are O(n) worst case.  The Trie structure requires that all nodes are accessed in each of these operations.

