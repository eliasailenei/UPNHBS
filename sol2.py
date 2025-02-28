import math

def sieve_upto(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime, [x for x in range(2, n + 1) if is_prime[x]]

def is_prime_trial(n, small_primes=None):
    if n < 2:
        return False
    if n < 4:
        return True  
    if n % 2 == 0 or n % 3 == 0:
        return (n == 2 or n == 3)

    limit = int(math.isqrt(n))
    if small_primes:
        for p in small_primes:
            if p > limit:
                break
            if n % p == 0:
                return (n == p)  
    else:
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
    return True

def extract_primes(binary_str, N):
    candidates = set()
    length = len(binary_str)
    prefix = [0] * (length + 1)
    for i in range(length):
        prefix[i+1] = (prefix[i] << 1) + (binary_str[i] == '1')

    for start in range(length):
        for end in range(start + 1, length + 1):
            val = prefix[end] - (prefix[start] << (end - start))
            if val >= N:
                break
            if val > 1:
                candidates.add(val)

    if not candidates:
        return []

    max_candidate = max(candidates)
    SIEVE_THRESHOLD = 500_000  

    primes_found = []
    if max_candidate <= SIEVE_THRESHOLD:
        is_prime_small, _ = sieve_upto(max_candidate)
        for val in sorted(candidates):
            if is_prime_small[val]:
                primes_found.append(val)
    else:
        is_prime_small, small_primes = sieve_upto(SIEVE_THRESHOLD)
        for val in sorted(candidates):
            if val <= SIEVE_THRESHOLD:
                if is_prime_small[val]:
                    primes_found.append(val)
            else:
                if is_prime_trial(val, small_primes):
                    primes_found.append(val)

    return format_prime_output(primes_found)

def format_prime_output(primes):
    if not primes:
        return "No primes found."
    count = len(primes)
    if count < 6:
        return f"{count}: {', '.join(map(str, primes))}"
    else:
        return (f"6: {primes[0]}, {primes[1]}, {primes[2]}, ..., "
                f"{primes[-3]}, {primes[-2]}, {primes[-1]}")

if __name__ == "__main__":
   print(extract_primes(input("Enter binary string: "), int(input("Enter N: "))))
