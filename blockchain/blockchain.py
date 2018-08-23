import hashlib as hasher
import datetime as date


class Block:
    """
    create blocks for block chain
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(
            bytes(
                str(self.index) + str(self.timestamp) + str(self.data) + str(
                    self.previous_hash), 'utf-8'))
        return sha.hexdigest()


class BlockChain:
    """
    block chain class, create genesis block and next blocks
    """
    def __init__(self):
        self.init_block = Block(0, date.datetime.now(), "Genesis Block", "0")
        self.num_blocks = 0
        self.blockchain = [self.init_block]

    def create_genesis_block(self):
        #  Manually construct a block with index 0 and arbitrary previous hash
        return self.init_block

    def next_block(self, last_block):
        self.num_blocks = self.num_blocks + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block " + str(self.num_blocks)
        this_hash = last_block.hash
        next_block = Block(self.num_blocks, this_timestamp, this_data, this_hash)
        self.blockchain.append(next_block)
        return next_block

    def get_blockchain(self):
        return self.blockchain

    def get_block(self, index):
        return self.blockchain[index]

    @staticmethod
    def print_block(block):
        print('------------start of block-----------\n')
        print('previous hash  : ' + str(block.previous_hash) + '\n')
        print('index          : ' + str(block.index) + '\n')
        print('timestamp      : ' + str(block.timestamp) + '\n')
        print('data           : ' + str(block.data) + '\n')
        print('this hash      : ' + str(block.hash + '\n'))
        print('----------end of this block----------\n')

    def print_blockchain(self):
        for block in self.blockchain:
            self.print_block(block)

    def validate_blockchain(self):
        for i in range(1, self.num_blocks + 1):
            if self.blockchain[i].previous_hash == self.blockchain[i-1].hash_block():
                print('Block ' + str(i-1) + ' is validated!\n')
            else:
                print('Block ' + str(i-1) + ' is changed!\n')
                return False
        return True

    def set_block(self, index, data):
        self.blockchain[index].data = data
