import hashlib 
import time
import numpy as np 
import matplotlib.pyplot as plt 

def generate_hash(message, previous_hash, nonce):
    sha = hashlib.sha256() 
    sha.update(str(message).encode('utf-8') +
                str(previous_hash).encode('utf-8') +
                str(nonce).encode('utf-8'))
    
    return sha.hexdigest() 

    
def pow_real(difficulty_level):
    message = "Hello World!"
    nonce = 0 
    previous_hash = "00008b0cf9426cc3ac02dd19bcff819aa5ea5c66ce245352e10614ab22ed0f64"
    hash = generate_hash(message, previous_hash, nonce)
    hashes = 0
    target = "0" * difficulty_level
    
    while hash[:difficulty_level] != target:
        nonce += 1
        hashes += 1
        hash = generate_hash(message, previous_hash, nonce)
    return hashes


def avg_hash_power(difficulty_level):
#    start_time = time.perf_counter()
#    hashes = pow_real(difficulty_level) 
#    end_time = time.perf_counter()
#    real_time = end_time - start_time
#    return hashes / real_time
    hash_powers = []
    for _ in range(5):
        start = time.perf_counter()
        pow_real(difficulty_level)
        end = time.perf_counter()
        hash_powers.append((16 ** difficulty_level) / (end - start))
    return np.mean(hash_powers)


def pow_sim(difficulty_level):
    # p is success chance
    p = 1 / (16 ** difficulty_level)
    attempts = np.random.geometric(p)
    hash_power = avg_hash_power(difficulty_level)
    return attempts / hash_power


def compare(difficulty_level):
    real_times = []
    sim_times = []
    for _ in range(30):
        start_time = time.perf_counter()
        pow_real(difficulty_level) 
        end_time = time.perf_counter()
        real_time = end_time - start_time
        real_times.append(real_time)
        sim_times.append(pow_sim(difficulty_level))

    plt.boxplot([real_times, sim_times], labels=['Actual', 'Simulator'])
    plt.ylabel('Elapsed Time')
    plt.show()


def main():
   difficulty_level = 5
   start_time = time.perf_counter()
   pow_real(difficulty_level) 
   end_time = time.perf_counter()
   actual_time = end_time - start_time
   
   sim_time = pow_sim(difficulty_level)
   print(f"Simulated Time: {sim_time}")
   print(f"Actual Time: {actual_time}")
   compare(difficulty_level)



if __name__=="__main__":
    main()

