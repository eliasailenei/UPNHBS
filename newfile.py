import time

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

    return {i for i, is_prime in enumerate(primes) if is_prime}

def get_substrings(binary, n):
    """Extracts unique decimal values from binary substrings, pruning large values early."""
    substrings = set()
    length = len(binary)
    for i in range(length):
        num = 0
        for j in range(i, length):
            num = (num << 1) | int(binary[j])  # Faster binary conversion
            if num >= n:
                break  # Stop early if number is too large
            substrings.add(num)
    return substrings

def find_primes(binary, n):
    """Finds unique prime numbers hidden in a binary string that are < N."""
    primes = sieve(n)
    substrings = get_substrings(binary, n)
    result_primes = [x for x in substrings if x in primes]
    result_primes.sort()

    if len(result_primes) < 6:
        return f"{len(result_primes)}: {', '.join(map(str, result_primes))}"
    return f"6: {', '.join(map(str, result_primes[:3]))}, ..., {', '.join(map(str, result_primes[-3:]))}"

# Example usage
if __name__ == "__main__":
    binary_str = input("Please enter the binary string: ")
    n = int(input("Please enter the value of N: "))
    start_time = time.time()
    print(find_primes(binary_str, n))
    print("--- %s seconds ---" % (time.time() - start_time))
