### Autocomplete with TRIES

#### Companion file - problem_5.ipynb

#### Description:
For this problem, I chose to implement the Trie class insert() and find() methods using a simple for loop statement, which simply checks if each character in the word or suffix is in the Trie Node or it's children.  The second part of this challenge was returning the suffixes for a user supplied prefix.  This was much more challenging.  The solution I found was to Recursively loop through the child nodes, while yielding the suffix when node.is_word was True.  I tried many different ways to do this with a Return statement and I couldn't get it to work.  The new Python 3 feature "yield from" really saved the day, and allowed me to return the suffix to the original calling function from deep within the Recursive Stack, while continuing the Recursive process.

#### Time Complexity:
The time complexity for insert() and suffixes() are O(n) worst case simplified O(nm), where n is the number of words, and m is the length of the longest word, or number of possible characters.  Given that in the English language there are 26 possible, characters, but no English word uses all 26, this makes sense.  Therefore, m is limited by the longest word in the input.  The time complexity for suffix() is also O(n), where n is the number of elements in the Trie below the input element.

#### Space Complexity:
Space complexity for the Trie is linear O(n) as well since each character is associated with one node and the number of characters is words(n) x possible characters(m) with auxillary space O(1).
