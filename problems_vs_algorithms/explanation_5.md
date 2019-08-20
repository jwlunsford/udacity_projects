### Autocomplete with TRIES

#### Companion file - problem_5.ipynb

For this problem, I chose to implement the Trie class Insert() and Delete() methods using a simple for loop statement, which simply checks if each character in the word or suffix is in the Trie Node or it's children.  The second part of this challenge was returning the suffixes for a user supplied prefix.  This was much more challenging.  The solution I found was to Recursively loop through the child nodes, while yielding the suffix when node.is_word was True.  I tried many different ways to do this with a Return statement and I couldn't get it to work.  The new Python 3 feature "yield from" really saved the day, and allowed me to return the suffix to the original calling function from deep within the Recursive Stack, while continuing the Recursive process.

#### Time and Space Complexity:

The time complexity for insert() and find() are O(n) worst case.  The time complexity for suffix() is also O(n), where n is the number of elements in the Trie below the input element.  Space complexity for the Trie is O(n) worse case.
