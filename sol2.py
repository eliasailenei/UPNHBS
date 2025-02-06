import time
import multiprocessing

def sieve(limit):
    """Generate a list of prime numbers up to the given limit using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False

    return {num for num, prime in enumerate(is_prime) if prime}

# Precompute primes up to 10 million
SMALL_PRIMES = sieve(10_000_000)

def is_prime(n):
    """Efficient prime check using precomputed primes and trial division."""
    if n in SMALL_PRIMES:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n < 10_000_000:  # Checked by the sieve
        return False
    # Trial division for larger numbers
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def process_substrings(args):
    """Parallel processing function to extract unique prime numbers from a binary substring."""
    binary, N, start, end = args
    primes = set()
    checked_nums = set()
    
    for i in range(start, end):
        num = 0
        for j in range(i, len(binary)):
            num = (num << 1) | (binary[j] == '1')  # Fast binary conversion
            if num >= N:  # Stop early if number exceeds limit
                break
            if num not in checked_nums:  # Avoid redundant calculations
                checked_nums.add(num)
                if is_prime(num):
                    primes.add(num)
    
    return primes

def extract_primes(binary, N):
    """Extract unique prime numbers from binary substrings with a hybrid execution strategy."""
    length = len(binary)

    # **Hybrid approach**
    if length < 100:  # Small cases, run single-threaded
        primes = set()
        checked_nums = set()

        for i in range(length):
            num = 0
            for j in range(i, length):
                num = (num << 1) | (binary[j] == '1')  # Fast binary conversion
                if num >= N:
                    break
                if num not in checked_nums:
                    checked_nums.add(num)
                    if is_prime(num):
                        primes.add(num)

    else:  # Large cases, use multiprocessing
        num_cores = multiprocessing.cpu_count()
        chunk_size = length // num_cores
        tasks = [(binary, N, i * chunk_size, (i + 1) * chunk_size) for i in range(num_cores)]
        tasks[-1] = (binary, N, (num_cores - 1) * chunk_size, length)

        with multiprocessing.Pool(num_cores) as pool:
            results = pool.map(process_substrings, tasks)

        primes = set().union(*results)

    # Sort primes
    primes = sorted(primes)

    # Formatting the output
    if not primes:
        return "No primes found."
    elif len(primes) < 6:
        return f"{len(primes)}: {', '.join(map(str, primes))}"
    else:
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(map(str, primes[-3:]))}"

if __name__ == "__main__":
    # Running tests
    test_cases = [
        ("0100001101001111", 999999),  # Small case
        ("01000011010011110100110101010000", 999999),  # Small case
        ("1111111111111111111111111111111111111111", 999999),  # Small case
        ("010000110100111101001101010100000011000100111000", 999999999),  # Medium
        ("0100001101001111010011010101000000110001001110000110001", 123456789012),  # Medium
        ("010000110100111101001101010100000011000100111000011000100111001", 123456789012345),  # Medium
        ("01000011010011110100110101010000001100010011100001100010011100100100001", 123456789012345678),  # Large
        ("0100001101001111010011010101000000110001001110000110001001110010010000101000001", 1234567890123456789),  # Large
        ("010000110100111101001101010100000011000100111000011000100111001001000010100000101000100", 1234567890123456789),  # Large
        ("01000011010011110100110101010000001100010011100001100010011100100100001010000010100010001010011", 12345678901234567890)  # Large
    ]

    for idx, (binary_str, n) in enumerate(test_cases):
        print(f"Test case {idx + 1}:")
        start_time = time.time()
        print(extract_primes(binary_str, n))
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.6f} seconds\n")
