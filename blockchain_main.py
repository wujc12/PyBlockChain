from blockchain.blockchain import BlockChain


blockchain = BlockChain()

# create the genesis block
previous_block = blockchain.create_genesis_block()

#  How many blocks should we add to the chain after the genesis block
num_of_blocks_to_add = 20

for i in range(num_of_blocks_to_add):
    next_block = blockchain.next_block(previous_block)
    previous_block = next_block

# print the whole block chain
# blockchain.print_blockchain()

# don't change block in the blockchain, and print the validation result
bl = blockchain.validate_blockchain()
print(bl)

# change block in the blockchain, and print the validation result
blockchain.set_block(4, 'Hey, I am block changed!')
bl = blockchain.validate_blockchain()
print(bl)
