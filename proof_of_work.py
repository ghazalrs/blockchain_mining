import hashlib # hashlib module is used for calculating hashes

def generate_hash(message, previous_hash, nonce):
    """
    The function ombines three pieces of information:the message, the previous hash, and the nonce
    and encodes them as bytes before computing the hash.
    """
    sha = hashlib.sha256() # initializes the SHA-256 algorithm
    # takes the input string (message + previous hash + nonce) and converts it into bytes
    sha.update(str(message).encode('utf-8') +
                str(previous_hash).encode('utf-8') +
                str(nonce).encode('utf-8'))
    
    return sha.hexdigest() # return the final hash value in hexadecimal
    
def proof_of_work(message, difficulty_level):
    """
    The function implenents the PoW algorithm.
    It solves the puzzle.
    Takes two parameters: message and difficulty level.
    Tires different nonce values until it finds one that satisfies the target condition.
    """
    nonce = 0 # start with a nonce of 0
    # a sample previous_hash to simulate linking to a previous block in a blockchain
    previous_hash = "00008b0cf9426cc3ac02dd19bcff819aa5ea5c66ce245352e10614ab22ed0f64"
    hash = generate_hash(message, previous_hash, nonce)
    trials = 0
    target = "0" * difficulty_level
    
    while hash[:difficulty_level] != target:
        """
        The while loop checks if the current hash starts with the required number of zeros.
        If not, increment the nonce and regenerate the hash.
        Each iteration counts as one trial.
        When a hash meeting the difficulty condition is found, the loop stops.
        The function prints both the nonce and the total number of trials.
        """
        nonce += 1
        trials += 1
        hash = generate_hash(message, previous_hash, nonce)
    print(nonce)
    print(trials)



def main():
   message = "Hello World!"
   difficulty_level = 2
   proof_of_work(message, difficulty_level) 


if __name__=="__main__":
    main()

