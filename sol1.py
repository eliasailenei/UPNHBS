import time
import math
import functools
import random
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def pollards_rho(n, max_attempts=5):
    if n % 2 == 0:
        return 2
    for _ in range(max_attempts):
        x = random.randint(2, n - 1)
        y = x
        c = random.randint(1, n - 1)
        d = 1
        
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
            if d == n:
                break
        if 1 < d < n:
            return d  
    return None  
def sieve(limit):
    is_prime_arr = bytearray(b'\x01') * (limit + 1)
    is_prime_arr[:2] = b'\x00\x00'
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime_arr[i]:
            is_prime_arr[i * i:limit+1:i] = b'\x00' * ((limit - i * i) // i + 1)
    return [i for i, prime in enumerate(is_prime_arr) if prime]
SMALL_PRIMES_LIST = sieve(10_000_000)
SMALL_PRIMES = set(SMALL_PRIMES_LIST)
def is_prime(n):
    if n < 2:
        return False
    if n in SMALL_PRIMES:
        return True
    if any(n % p == 0 for p in SMALL_PRIMES_LIST if p * p <= n):
        return False  
    if n < 10**12:  
        factor = pollards_rho(n)
        if factor and factor != n:
            return False  
    return True  
def get_candidates(binary, N):
    length = len(binary)
    prefix = [0] * (length + 1)
    for i in range(length):
        prefix[i+1] = (prefix[i] << 1) + (1 if binary[i] == '1' else 0)
    candidates = set()
    for i in range(length):
        for j in range(i+1, length+1):
            val = prefix[j] - (prefix[i] << (j - i))
            if val >= N:
                break
            if val > 1 and (val == 2 or val % 2 != 0):  
                candidates.add(val)
    return candidates
def extract_primes(binary, N):
    if not binary or not binary.strip("0"):
        return "No primes found."
    candidates = get_candidates(binary, N)
    candidates = sorted(n for n in candidates if n > 1)
    if not candidates:
        return "No primes found."
    results = [n for n in candidates if is_prime(n)]
    primes = sorted(results)
    if not primes:
        return "No primes found."
    elif len(primes) < 6:
        return f"{len(primes)}: {', '.join(map(str, primes))}"
    else:
        last_three = [f"{n}" for n in primes[-3:]]
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(last_three)}"
if __name__ == "__main__":
    print(extract_primes(input("Enter a binary string: "), int(input("Enter N: "))))
