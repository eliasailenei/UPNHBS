def binary_to_decimal(binary_str):
    """Convert a binary string to a decimal integer."""
    return int(binary_str, 2)

def find_prime(limit):
    """Find all prime numbers up to a given limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return set()
    try:
        primes = [True] * (limit + 1)  # just in case its too big
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for num in range(2, int(limit ** 0.5) + 1):
            if primes[num]:
                for multiple in range(num * num, limit + 1, num):
                    primes[multiple] = False
        return {num for num, is_prime in enumerate(primes) if is_prime}
    except (MemoryError, OverflowError):
        return None  # Too big for the sieve

def is_prime_backup(n):
    """Backup prime check using trial division"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def extract_primes(binary_string, N):
    """Extract prime numbers from binary string, using the sieve or fallback method."""
    decimal_values = set()
    length = len(binary_string)
    for i in range(length):
        num = 0
        for j in range(i, length):
            num = (num << 1) | int(binary_string[j])  # Efficient binary conversion
            if num >= N:
                break  # Stop if the number is too large
            decimal_values.add(num)

    # Try using the sieve method
    prime_set = find_prime(N)
    
    if prime_set is not None:
        primes = sorted(decimal_values.intersection(prime_set))
    else:
        # If sieve failed, fall back to individual prime checking
        primes = sorted(num for num in decimal_values if is_prime_backup(num))

    # Output format
    if len(primes) == 0:
        print("0: No primes found")
    elif len(primes) < 6:
        print(f"{len(primes)}: {', '.join(map(str, primes))}")
    else:
        print(f"{len(primes)}: {', '.join(map(str, primes[:3]))}, {', '.join(map(str, primes[-3:]))}")

extract_primes(input("Please enter a binary string: "), input("Please enter a limit N: "))
