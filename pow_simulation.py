import hashlib 
import time
import numpy as np 
import matplotlib.pyplot as plt
import pingouin as pg 

def generate_hash(message, previous_hash, nonce):
    # creates a sha-256 object
    sha = hashlib.sha256() 

    # converting to string and encoding to bytes and concatenation 
    sha.update(str(message).encode('utf-8') +
                str(previous_hash).encode('utf-8') +
                str(nonce).encode('utf-8'))
    
    # computes final hash and returns a hex string 
    return sha.hexdigest() 

    
def pow_real(difficulty_level):
    message = "Hello World!"
    nonce = 0 
    previous_hash = "00008b0cf9426cc3ac02dd19bcff819aa5ea5c66ce245352e10614ab22ed0f64"
    hash_val = generate_hash(message, previous_hash, nonce)
    hashes = 0
    # the required prefix of a valid hash
    target = "0" * difficulty_level 
    
    while hash_val[:difficulty_level] != target:
        nonce += 1
        hashes += 1
        hash_val = generate_hash(message, previous_hash, nonce)
    return hashes

# estimates hashes per second based on the difficulty level
def avg_hash_power(difficulty_level):
    hash_powers = []
    # use a for loop for multiple measurements 
    for _ in range(10):
        start = time.perf_counter()
        pow_real(difficulty_level)
        end = time.perf_counter()
        hash_powers.append((16 ** difficulty_level) / (end - start))
    return np.mean(hash_powers)


def pow_sim(difficulty_level, hash_power):
    # probability of success
    p = 1 / (16 ** difficulty_level) 

    # use geometric distribution to simulate how many attempts it takes until first success
    attempts = np.random.geometric(p)

    # attempts = 1 / p

    # returns the simulated time taken to mine a block
    return attempts / hash_power


def compare(difficulty_level):
    # compare actual time vs simulated time
    real_times = []
    sim_times = []
    hash_power = avg_hash_power(difficulty_level)
    for _ in range(30):
        start_time = time.perf_counter()
        pow_real(difficulty_level) 
        end_time = time.perf_counter()
        real_time = end_time - start_time
        real_times.append(real_time)
        sim_times.append(pow_sim(difficulty_level, hash_power))

    # run a tost equivalence test between actual times and simulated times
    tost = pg.tost(real_times, sim_times)
    print(tost)

    plt.boxplot([real_times, sim_times], labels=['Actual', 'Simulator'])
    plt.ylabel('Elapsed Time')
    plt.show()


# simulate a race between two miners with different hash powers
def hash_power_competition(difficulty_level):
   node_a_wins = 0
   node_b_wins = 0

   # runs 1000 simulated races 
   for _ in range(1000):
       node_a = pow_sim(difficulty_level, 1)
       node_b = pow_sim(difficulty_level, 2)
       if node_a < node_b:
           node_a_wins += 1
       else:
           node_b_wins += 1
   node_a_win_rate = node_a_wins / 1000
   node_b_win_rate = node_b_wins / 1000

   # prints which node wins more often overall
   if node_a_win_rate > node_b_win_rate:
       print("Node A wins!")
   else:
       print("Node B wins!")

def main():
   difficulty_level = 4
   start_time = time.perf_counter()
   pow_real(difficulty_level) 
   end_time = time.perf_counter()
   actual_time = end_time - start_time
   hash_power = avg_hash_power(difficulty_level)
   sim_time = pow_sim(difficulty_level, hash_power)
   print(f"Simulated Time: {sim_time}")
   print(f"Actual Time: {actual_time}")
   compare(difficulty_level)
   hash_power_competition(difficulty_level)



if __name__=="__main__":
    main()

