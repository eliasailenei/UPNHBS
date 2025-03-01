import math
def sieve(limit): # this method has a limit btw
    is_prime_arr = bytearray(b'\x01') * (limit + 1) # we use bytearray for better performance. numbers use more memory and we are very stingy with memory
    is_prime_arr[:2] = b'\x00\x00'  # 0 and 1 are not prime
    for i in range(2, math.isqrt(limit) + 1): # all non-prime numbers have a prime factor less than or equal to their square root
        if is_prime_arr[i]: # if its a prime number
            is_prime_arr[i * i:limit+1:i] = b'\x00' * ((limit - i * i) // i + 1) #looks like gibberish but we are using slice assignment to set all multiples of i to 0
    return [i for i, prime in enumerate(is_prime_arr) if prime] # return all prime numbers 
SMALL_PRIMES_LIST = sieve(10_000_000) # generate a list of small primes
SMALL_PRIMES = set(SMALL_PRIMES_LIST) # ensure no duplicates
def is_prime(n): # trial division method (very slow but we have no choice)
    if n < 2: # 0 and 1 are not prime
        return False
    if n in SMALL_PRIMES: # already computed
        return True
    if n % 2 == 0 or n % 3 == 0: # check if n is divisible by 2 or 3
        return False
    r = math.isqrt(n) # get the square root of n
    for p in SMALL_PRIMES_LIST: # check if n is divisible by any of the small primes
        if p > r: # if the prime is greater than the square root of n, then n is prime
            return True  
        if n % p == 0: # if n is divisible by p, then n is not prime
            return False
    i = 5 # start from 5
    while i <= r: # check if n is divisible by any number of the form 6k +/- 1
        if n % i == 0 or n % (i + 2) == 0: # if n is divisible by i or i + 2, then n is not prime
            return False
        i += 6 # increment i by 6
    return True
def get_candidates(binary, N): # get all possible numbers from the binary string
    length = len(binary) # get the length of the binary string
    prefix = [0] * (length + 1) # create a list of zeros with length + 1 
    for i in range(length):
        prefix[i+1] = (prefix[i] << 1) + (1 if binary[i] == '1' else 0) # convert the binary string to decimal
    candidates = set() # use a set to avoid duplicates
    for i in range(length): # get all possible numbers from the binary string yk the rest ...
        for j in range(i+1, length+1): 
            val = prefix[j] - (prefix[i] << (j - i))
            if val >= N:
                break
            if val > 1 and (val == 2 or val % 2 != 0):  
                candidates.add(val)
    return candidates
def extract_primes(binary, N):
    candidates = get_candidates(binary, N) # get all possible numbers from the binary string
    candidates = sorted(n for n in candidates if n > 1) # sort the numbers
    if not candidates:
        return "No primes found."
    results = [n for n in candidates if is_prime(n)] # get all prime numbers from the candidates
    primes = sorted(results)
    if not primes:
        return "No primes found."
    elif len(primes) < 6: # if we have less than 6 primes
        return f"{len(primes)}: {', '.join(map(str, primes))}"
    else: # if we have more than 6 primes
        last_three = [f"{n}" for n in primes[-3:]]
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(last_three)}"
if __name__ == "__main__": 
    print(extract_primes(input("Enter a binary string: "), int(input("Enter N: "))))