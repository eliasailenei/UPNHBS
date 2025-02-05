import time

def is_prime(n):
    """Efficient trial division method to check primality."""
    if n < 2:
        return False
    if n in {2, 3, 5, 7}:
        return True  # Quick lookup for small primes
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def extract_primes(binary, N):
    """Extract unique prime numbers from binary substrings."""
    primes = set()
    length = len(binary)
    
    for i in range(length):
        num = 0  # Convert binary substrings on the fly
        for j in range(i, length):
            num = (num << 1) | int(binary[j])
            if num >= N:  # Stop if number exceeds limit
                break
            if num not in primes and is_prime(num):
                primes.add(num)
    
    primes = sorted(primes)
    
    # Formatting the output
    if not primes:
        return "No primes found."
    elif len(primes) < 6:
        return f"{len(primes)}: {', '.join(map(str, primes))}"
    else:
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(map(str, primes[-3:]))}"

# Test cases
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

# Running the tests
for idx, (binary_str, n) in enumerate(test_cases):
    print(f"Test case {idx + 1}:")
    start_time = time.time()
    print(extract_primes(binary_str, n))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds\n")
