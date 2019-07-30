import sys

class HuffmanNode(object):

    def __init__(self, char, freq):
        """initialize the node"""
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


class HuffmanTree(object):

    def __init__(self, data):
        self.root = None
        self.heap = list()
        self.codes = {}
        self.bitstream = ''
        self.data = data

    def get_codes(self):
        return self.codes

    def get_heap(self):
        return self.heap

    def get_root(self):
        return self.root

    def get_bitstream(self):
        return self.bitstream

    def get_data(self):
        return self.data

    def get_char_freq(self):
        # create a dictionary of frequency values where key = character
        characters = self.get_data()
        frequency = {}
        for c in characters:
            if c not in frequency:
                frequency[c] = 0
            frequency[c] += 1
        return frequency

    def sort_by_freq(self):
        # sort the heap
        heap = self.get_heap()
        heap.sort(key=lambda x: x.freq, reverse=True)  # need reverse here because pop takes from the end of list

    def build_tree(self):
        heap = self.get_heap()
        # create a leaf node for each unique character and build a min heap for all leaf nodes
        frequency = self.get_char_freq()
        # handle case where all characters are the same, throw error code -1
        if len(frequency) == 1:
            for char, freq in frequency.items():
                node = HuffmanNode(char, freq)
            self.codes[char] = '0'
            self.root = node
            return -1
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heap.append(node)

        # make sure heap is sorted
        self.sort_by_freq()

        # while heap has more than one node, combine the smallest two
        while len(heap) > 1:
            node1 = heap.pop()
            node2 = heap.pop()
            # print(f'{node1.char}, {node1.freq}')  # can remove when done testing
            # print(f'{node2.char}, {node2.freq}')  # can remove when done testing

            # combine the nodes
            new_node = HuffmanNode(None, node1.freq + node2.freq)
            new_node.left = node1
            new_node.right = node2

            # append the newly combined node to the heap and resort
            heap.append(new_node)
            self.sort_by_freq()

        # return the remaining item
        self.root = heap[0]
        return 0

    def make_codes(self):
        current_code = ''
        root = self.get_root()

        def traverse(node, current_code):
            # traverse tree inorder - recursive solution
            if node == None:      # node has to be something
                return

            if node != None:
                # visit node
                if node.char != None:
                    self.codes[node.char] = current_code
                    return

            # traverse left
            traverse(node.get_left_child(), current_code + '0')

            # traverse right
            traverse(node.get_right_child(), current_code + '1')

        traverse(root, current_code)

    def create_bitstream(self):
        # create the bitstream by reading the codes for each character in data
        data = self.get_data()
        codes = self.get_codes()

        # for each character in the original data, lookup it's bit value and append it to the output
        for char in data:
            self.bitstream += codes[char]

    def decode(self, data):
        # decode the tree bit-by-bit.
        node = self.get_root()
        stream = data
        decode = ''

        # case where all data characters are the same (e.g.; 'aaaaaa')
        if node.get_right_child() == None and node.get_left_child() == None:
            decode = node.char * node.freq
        else:
            # normal case, loop through the bitstream
            for bit in stream:
                # if bit is 0 go left, if 1 go right
                if bit == '0':
                    node = node.get_left_child()
                    if node.char == None:  # this is an internal node
                        continue
                    else:
                        decode += node.char
                        node = self.get_root()
                if bit == '1':
                    node = node.get_right_child()
                    if node.char == None:  # this is an internal node
                        continue
                    else:
                        decode += node.char
                        node = self.get_root()

        return decode


def huffman_encoding(data):
    # build a huffman tree from the character frequencies found in data.
    if data == '':
        print(f'Data cannot be null, please enter valid characters')
    else:
        tree = HuffmanTree(data)
        val = tree.build_tree()
        if val == 0:
            # normal case, proceed with make codes
            tree.make_codes()
            tree.create_bitstream()
            return tree.bitstream, tree
        else:
            tree.create_bitstream()
            return tree.bitstream, tree

def huffman_decoding(data, tree):
    # traverse the tree, for each 0-bit in data move left and 1-bit move right, do this until reaching a leaf node
    return tree.decode(data)


if __name__ == "__main__":

    # TEST 1 - Normal data
    a_great_sentence = "The bird is the word"

    print("***** TEST 1 *****")
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))



    # TEST 2 - Outlier, All characters the same
    a_great_sentence = "aaaaaaaa"

    print("***** TEST 2 (Edge case) *****")
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


    # TEST 3 - Edge case, null data
    a_great_sentence = ""

    print("***** TEST 3 (Edge case)*****")
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    if a_great_sentence != "":
        encoded_data, tree = huffman_encoding(a_great_sentence)

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

    else:
        print(f'ERROR:  Cannot compute! Data must not be Null')

