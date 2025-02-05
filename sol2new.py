import heapq,time

def sieve(limit):
    """Returns a set of prime numbers up to 'limit' using the Sieve of Eratosthenes."""
    if limit < 2:
        return set()
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not prime
    
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    
    return {i for i in range(limit + 1) if primes[i]}

def is_prime(n, prime_set, small_primes):
    """Checks if a number is prime using small primes and trial division."""
    if n in prime_set:
        return True
    if n < 2 or any(n % p == 0 for p in small_primes if p * p <= n):
        return False
    return True

def binary_to_decimal(binary_str):
    """Converts a binary string to its decimal equivalent."""
    return int(binary_str, 2)

def get_substrings(binary, n):
    """Extracts unique decimal values from binary substrings, pruning large values early."""
    substrings = set()
    length = len(binary)
    for i in range(length):
        num = 0
        for j in range(i, length):
            num = (num << 1) | (int(binary[j]))  # Faster binary conversion
            if num >= n:
                break  # Stop early if number is too large
            substrings.add(num)
    return substrings

def ans(binary, n):
    """Finds unique prime numbers hidden in a binary string that are < N."""
    all_subs = get_substrings(binary, n)
    all_subs.discard(0)  # Remove 0 explicitly
    all_subs.discard(1)  # Remove 1 explicitly
    
    # Use small sieve for numbers up to sqrt(N)
    small_limit = int(n ** 0.5) + 1
    small_primes = sieve(small_limit)
    prime_set = sieve(n) if n <= 10**7 else set()  # Avoid large sieve for huge N
    
    primes = [x for x in all_subs if is_prime(x, prime_set, small_primes)]
    primes.sort()  # Sorting required for ordered output
    
    # Format output
    if len(primes) == 0:
        return "No primes found."
    elif len(primes) < 6:
        return f"{len(primes)}: {', '.join(map(str, primes))}"
    else:
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(map(str, primes[-3:]))}"  # Print first 3 and last 3

# Get user input
test_cases = [
    ("0100001101001111", 999999),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999), # sus
    ("010000110100111101001101010100000011000100111000", 999999999),
    ("0100001101001111010011010101000000110001001110000110001", 123456789012),
    ("010000110100111101001101010100000011000100111000011000100111001", 123456789012345), # test cases 7 has only extra bits yet it takes more time to execute INVESTIGATE!
    ("01000011010011110100110101010000001100010011100001100010011100100100001", 123456789012345678),
    ("0100001101001111010011010101000000110001001110000110001001110010010000101000001", 1234567890123456789),
    ("010000110100111101001101010100000011000100111000011000100111001001000010100000101000100", 1234567890123456789),
    ("01000011010011110100110101010000001100010011100001100010011100100100001010000010100010001010011", 12345678901234567890)
]

# Loop through test cases
for idx, (binary_str, n) in enumerate(test_cases):
    print(f"Test case {idx + 1}:")
    start_time = time.time()
    print(ans(binary_str, n))
    end_time = time.time()
    
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")