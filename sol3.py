import math,random 
def sieve_segment(low, high):
    sieve_range = high - low + 1
    is_prime = [True] * sieve_range
    if low == 1: is_prime[0] = False
    limit = int(math.sqrt(high))
    small_primes = sieve_upto(limit)[1]
    for prime in small_primes:
        start = max(prime * prime, low + (prime - low % prime) % prime)
        for j in range(start, high + 1, prime):
            is_prime[j - low] = False
    return is_prime, [low + i for i in range(sieve_range) if is_prime[i]]
def sieve_upto(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime, [x for x in range(2, n + 1) if is_prime[x]]
def is_prime_trial(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    limit = int(math.sqrt(n))
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True
def is_prime_fermat(n, k=5):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1: return False
    return True
def pollards_rho(n):
    if n % 2 == 0: return 2
    x = random.randint(2, n - 1); y = x; c = random.randint(1, n - 1); d = 1
    def f(x): return (x * x + c) % n
    while d == 1: x = f(x); y = f(f(y)); d = math.gcd(abs(x - y), n)
    return d if d != n else None
def is_prime_large(n):
    if is_prime_fermat(n): return True
    factor = pollards_rho(n)
    if factor and factor != n: return False
    return True
def extract_primes(binary_str, N):
    if not all(index in "01" for index in binary_str): return "0: Invalid binary strings"
    if type(N) is not int: return "0: Invalid N given"
    candidates = set()
    length = len(binary_str)
    prefix = [0] * (length + 1)
    for i in range(length):
        prefix[i+1] = (prefix[i] << 1) + (binary_str[i] == '1')
    for start in range(length):
        for end in range(start + 1, length + 1):
            val = prefix[end] - (prefix[start] << (end - start))
            if val >= N: break
            if val > 1: candidates.add(val)
    if not candidates: return "No primes found."
    max_candidate = max(candidates)
    TRIAL_THRESHOLD = 10_000
    SIEVE_THRESHOLD = 10_000_000
    primes_found = []
    trial_checked = set()
    for val in sorted(candidates):
        if val <= TRIAL_THRESHOLD:
            if is_prime_trial(val):
                primes_found.append(val)
            trial_checked.add(val)
    medium_candidates = sorted(n for n in candidates if TRIAL_THRESHOLD < n <= SIEVE_THRESHOLD)
    if medium_candidates:
        low, high = min(medium_candidates), max(medium_candidates)
        is_prime_segmented, primes_from_sieve = sieve_segment(low, high)
        for val in medium_candidates:
            if val - low >= 0 and is_prime_segmented[val - low]:
                primes_found.append(val)
    for val in sorted(n for n in candidates if n > SIEVE_THRESHOLD):
        if is_prime_large(val):
            primes_found.append(val)
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