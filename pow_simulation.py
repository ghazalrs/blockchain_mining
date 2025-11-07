from proof_of_work import proof_of_work
def pow_sim(difficulty_level):
    # p is success chance
    p = 1 / difficulty_level
    attempts = 1 / p

    # compute hash rate H (hashes per second or attempts per second)
    hashes = nonce
    time_simulated = time
    hash_rate = hashes / time_simulated

    expected_time = attempts / hash_rate