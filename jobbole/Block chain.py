import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode("utf8") +
                   str(self.timestamp).encode("utf8") +
                   str(self.data).encode("utf8") +
                   str(self.previous_hash).encode("utf8"))
        return sha.hexdigest()

import datetime as date

def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
def next_block(block):
    return Block(block.index+1, date.datetime.now(), "Genesis Block", "0")

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)#next_block方法有问题，没有这个方法
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print("Block",block_to_add.index,"has been added to the blockchain!")
    print("Hash: {}\n".format(block_to_add.hash))