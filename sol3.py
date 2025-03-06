import math,random # built-in libs, allowed by spec
def sieve_segment(low, high): # sieve is going to gen numbers from x to y instead of 1 to n
    sieve_range = high - low + 1 
    is_prime = [True] * sieve_range # this will set all numbers to prime
    if low == 1: is_prime[0] = False
    limit = int(math.sqrt(high))
    small_primes = sieve_upto(limit)[1] # this will get the prime numbers
    for prime in small_primes: # this will iterate through the prime numbers
        start = max(prime * prime, low + (prime - low % prime) % prime) # this will get the start of the prime number
        for j in range(start, high + 1, prime): 
            is_prime[j - low] = False
    return is_prime, [low + i for i in range(sieve_range) if is_prime[i]] # this will return the prime numbers
def sieve_upto(n): # the main sieve function
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime, [x for x in range(2, n + 1) if is_prime[x]]
def is_prime_trial(n): # this is a simple trial division method to check if the number is prime
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    limit = int(math.sqrt(n)) # this will get the square root of the number and set the limit
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True
def is_prime_fermat(n, k=5): # this is the fermat primality test to check if the number is prime
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for _ in range(k): # this will iterate through the number
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1: return False
    return True
def pollards_rho(n): # this is the pollards rho algorithm to check if the number is prime
    if n % 2 == 0: return 2
    x = random.randint(2, n - 1); y = x; c = random.randint(1, n - 1); d = 1
    def f(x): return (x * x + c) % n
    while d == 1: x = f(x); y = f(f(y)); d = math.gcd(abs(x - y), n) # using the greatest common divisor to check if the number is prime
    return d if d != n else None
def is_prime_large(n): # this is the main function to check if the number is prime for a large N
    if is_prime_fermat(n): return True
    factor = pollards_rho(n)
    if factor and factor != n: return False
    return True
def extract_primes(binary_str, N): # the main function
    if not all(index in "01" for index in binary_str): return "0: Invalid binary strings" # edge case : only 0 and 1 are allowed
    if type(N) is not int: return "0: Invalid N given" # edge case : N must be an integer
    candidates = set() # no dupes allowed
    length = len(binary_str)
    prefix = [0] * (length + 1)
    for i in range(length): # this will convert the binary string to a decimal number
        prefix[i+1] = (prefix[i] << 1) + (binary_str[i] == '1')
    for start in range(length):
        for end in range(start + 1, length + 1):
            val = prefix[end] - (prefix[start] << (end - start))
            if val >= N: break
            if val > 1: candidates.add(val)
    if not candidates: return "No primes found."
    max_candidate = max(candidates)
    TRIAL_THRESHOLD = 10_000 # this is the threshold for the trial division (balanced)
    SIEVE_THRESHOLD = 10_000_000 # this is the threshold for the sieve (balanced)
    primes_found = []
    trial_checked = set()
    for val in sorted(candidates): # this will iterate through the candidates
        if val <= TRIAL_THRESHOLD: # if the number is less than the threshold, then it will use the trial division
            if is_prime_trial(val):  # if the number is prime, then it will add it to the list
                primes_found.append(val)
            trial_checked.add(val)
    medium_candidates = sorted(n for n in candidates if TRIAL_THRESHOLD < n <= SIEVE_THRESHOLD) # this will get the medium candidates
    if medium_candidates: # if there are medium candidates
        low, high = min(medium_candidates), max(medium_candidates) # get the min and max of the medium candidates
        is_prime_segmented, primes_from_sieve = sieve_segment(low, high)  # this will get the prime numbers from a limit
        for val in medium_candidates: 
            if val - low >= 0 and is_prime_segmented[val - low]: # if the number is prime, then it will add it to the list
                primes_found.append(val)
    for val in sorted(n for n in candidates if n > SIEVE_THRESHOLD): # if the number is greater than the threshold, then it will use the hybrid approach
        if is_prime_large(val):
            primes_found.append(val) # if the number is prime, then it will add it to the list
    if not primes_found:
        return "No primes found."
    count = len(primes_found)
    if count < 6:
        return f"{count}: {', '.join(map(str, primes_found))}"
    else:
        return (f"6: {primes_found[0]}, {primes_found[1]}, {primes_found[2]}, ..., "
                f"{primes_found[-3]}, {primes_found[-2]}, {primes_found[-1]}")
if __name__ == "__main__":
    print(extract_primes(input("Enter binary string: "), int(input("Enter N: "))))
    # Code made and maintained by Elias Andrew Ailenei (github.com/eliasailenei) 