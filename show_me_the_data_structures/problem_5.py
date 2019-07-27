import hashlib
from datetime import datetime


class Block(object):

    def __init__(self, data, timestamp=None):
        self.index = None   # will be set when added to the BlockChain
        if timestamp == None:
            self.timestamp = self.__make_timestamp(datetime.now())
        else:
            self.timestamp = timestamp
        self.data = data
        self.previous_hash = None
        self.next = None
        self.hash = self.__calc_hash()

    def __calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __make_timestamp(self, dt):
        return datetime.timestamp(dt)

    def __convert_to_utc_time(self):
        '''converts timestamp to utc time'''
        return datetime.utcfromtimestamp(self.timestamp)

    def __repr__(self):
        p_str = ''
        p_str += 'index: {self.index} \n'
        p_str += 'time: ' + str(self.__convert_to_utc_time()) + '\n'
        p_str += 'data: {self.data} \n'
        p_str += 'hash: {self.hash} \n'
        p_str += 'previous_hash: {self.previous_hash} \n'
        return p_str.format(self=self)


class BlockChain(object):

    def __init__(self):
        '''create the initial block, no params required'''
        self.init_block = None
        self.last_block = None
        self.next_index = 1


    def add_block(self, block):
        '''add a new block to the chain'''
        if self.init_block == None:                     # no block exists yet, so add this one and return
            self.init_block = block
            self.last_block = block
            block.index = self.next_index
            self.next_index += 1
            return
        else:
            prev_block = self.last_block            # retrieve the last block added
            block.previous_hash = prev_block.hash   # set the previous_hash for the new block
            block.index = self.next_index           # set the index for the new block
            prev_block.next = block                 # establish the link to the previous block
            self.last_block = block                 # move pointer for the last block
            self.next_index += 1                    # increment the chain index

    def get_block_by_index(self, idx):
        '''return the block at the specified index'''
        block = self.init_block
        while block:
            if block.index == idx:
                return block
            block = block.next
        print('Invalid Block Index ({})'.format(idx))

    def print_blocks(self):
        '''prints each block in sequential order'''
        if self.init_block == None:
            print('Empty Chain.  Please add a block\n')
            return
        block = self.init_block
        print('***** Printing blocks *****\n')
        while block:
            print(block)
            block = block.next
        print('***** End Print *****\n')


# TESTING

# Create Block1
data1 = 'some data to encode'
block1 = Block(data1)

# Create Block2
data2 = 'this message was hashed with sha256'
block2 = Block(data2)

# Create Block3, using the optional timestamp parameter
time = 1565499976
data3 = 'data data and more data'
block3 = Block(data3, time)

# create the blockchain
chain = BlockChain()
chain.print_blocks()                                # should return an empty chain message, as there are no blocks yet

# add the blocks
chain.add_block(block1)
chain.add_block(block2)
chain.add_block(block3)


chain.print_blocks()                                # print each block in sequential order

print(chain.get_block_by_index(3))                  # should print out block at index 2

chain.get_block_by_index(5)                         # should return an error message 'Invalid Block Index'

