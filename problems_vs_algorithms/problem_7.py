# HTTPRouter Using a TRIE

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = handler


    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # path should be a list.
        current_node = self.root

        for p in path:
            if p not in current_node.children:
                # add this path to children
                current_node.children[p] = RouteTrieNode()
            # get the node associated with this part
            current_node = current_node.children[p]

        # when the path ends, add the Handler to this node
        current_node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # path should be a list.
        current = self.root
        if len(path) == 1:
            # this is the root path
            return current

        for p in path:
            if p not in current.children:
                return None
            current = current.children[p]
        return current


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        # Insert the node as before
        self.children[path_part] = path_part


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(handler)


    def add_handler(self, path, handler):
        # Add a handler for a path ('/part1/part2/part3')
        # You will need to split the path and pass the parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        if path_list:
            self.route.insert(path_list, handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        f = self.route.find(path_list)

        # check for a None value, path was not found
        if f == None:
            return 'not found handler'
        else:
            return f.handler


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path.startswith('/') and path.endswith('/'):
            # slice the list to account for leading and trailing '/'
            path_list = path.split('/')[:-1]
        else:
            path_list = path.split('/')

        return path_list


# TESTING
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

