import hashlib # used to generate the SHA-256 hash of the block data
import datetime # used to record the timestamp of the block

class Block:
    """
    Block class contains the transaction data, the previous block's hash,
    the current block's hash, the nonce, and the timestamp.
    """

    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.hash = self.generate_hash()

    
    def generate_hash(self):
        """"
        The method concatenates the block's transaction data, the previous block's hash,
        timestamp, and nonce, and then generates the hash using the SHA-256 hashing algorithm
        """

        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        
        return sha.hexdigest()
    
    def mine_block(self, target_difficulty):
        """
        The method will implenent the PoW algorithm
        """

        while self.hash[:len(target_difficulty)] != target_difficulty:
            self.nonce += 1
            self.hash = self.generate_hash()
        print("Block mined:", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()] # chain is an empty list

    def create_genesis_block(self):
        """
        The genesis block is the first block on the blockchain, 
        and it does not have a previous block's hash
        """
        return Block("Genesis Block", "0")
    
    def add_block(self, new_block):
        """
        The method adds a new block to the chain by setting the previous block's hash
        and calling the mine_block method
        """
        new_block.previous_hash = self.chain[-1].hash
        new_block.mine_block("0000")
        self.chain.append(new_block)

blockchain = Blockchain()

block1 = Block("Transaction data 1", "")
blockchain.add_block(block1)

block2 = Block("Transaction data 2", "")
blockchain.add_block(block2)

block3 = Block("Transaction data 3", "")
blockchain.add_block(block3)

