import hashlib

def generate_hash(message, previous_hash, nonce):
    """
    The method takes the message, previous_hash, and nonce
    as input and generates the SHA-256 hash of the message 
    using hashlib module.
    """
    sha = hashlib.sha256()
    sha.update(str(message).encode('utf-8') +
                str(previous_hash).encode('utf-8') +
                str(nonce).encode('utf-8'))
    
    return sha.hexdigest()
    
def proof_of_work(message, difficulty_level):
    """
    The method implenents the PoW algorithm
    """
    nonce = 0
    trials = 0
    previous_hash = "00008b0cf9426cc3ac02dd19bcff819aa5ea5c66ce245352e10614ab22ed0f64"
    hash = generate_hash(message, previous_hash, nonce)
    target = "0" * difficulty_level
    while hash[:difficulty_level] != target:
        nonce += 1
        trials += 1
        hash = generate_hash(message, previous_hash, nonce)
    print(nonce)
    print(trials)



def main():
   message = "Hi this is Ghazal"
   difficulty_level = 2
   proof_of_work(message, difficulty_level) 


if __name__=="__main__":
    main()

