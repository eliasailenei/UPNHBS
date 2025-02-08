# made with love by Elias Andrew Ailenei (eliasailenei) and comments help from github copilot
import time
import math
import functools
import sympy # will be removed from final submission
def sieve(limit): # this method has a limit btw
    is_prime_arr = bytearray(b'\x01') * (limit + 1) # we use bytearray for better performance. numbers use more memory and we are very stingy with memory
    is_prime_arr[:2] = b'\x00\x00'  # 0 and 1 are not prime
    for i in range(2, math.isqrt(limit) + 1): # all non-prime numbers have a prime factor less than or equal to their square root
        if is_prime_arr[i]: # if its a prime number
            is_prime_arr[i * i:limit+1:i] = b'\x00' * ((limit - i * i) // i + 1) #looks like gibberish but we are using slice assignment to set all multiples of i to 0
    return [i for i, prime in enumerate(is_prime_arr) if prime] # return all prime numbers 
SMALL_PRIMES_LIST = sieve(10_000_000) # generate a list of small primes
SMALL_PRIMES = set(SMALL_PRIMES_LIST) # ensure no duplicates
@functools.lru_cache(maxsize=None) # cache the results of this function to avoid recomputation, this can be removed if not allowed
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
        last_three = [f"{n} --> {'✅' if sympy.isprime(n) else '❌'}" for n in primes[-3:]]
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(last_three)}"
if __name__ == "__main__": # our internal test cases, will be removed from final submission
    test_cases = [
        ("0100001101001111", 999999),
        ("01000011010011110100110101010000", 999999),
        ("1111111111111111111111111111111111111111", 999999),
        ("010000110100111101001101010100000011000100111000", 999999999),
        ("0100001101001111010011010101000000110001001110000110001", 123456789012),
        ("010000110100111101001101010100000011000100111000011000100111001", 123456789012345),
        ("01000011010011110100110101010000001100010011100001100010011100100100001", 123456789012345678),
        ("0100001101001111010011010101000000110001001110000110001001110010010000101000001", 1234567890123456789),
        ("010000110100111101001101010100000011000100111000011000100111001001000010100000101000100", 1234567890123456789),
        ("01000011010011110100110101010000001100010011100001100010011100100100001010000010100010001010011", 12345678901234567890)
    ]
    for idx, (binary_str, n) in enumerate(test_cases):
        print(f"Test case {idx + 1}:")
        start_time = time.time()
        print(extract_primes(binary_str, n))
        print(f"Time taken: {time.time() - start_time:.6f} seconds\n")
