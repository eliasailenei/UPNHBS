import math # built-in libs, allowed by spec
def sieve_upto(n): # this is a limit that the sieve will go up to since it has a memory limit and has a bad diminishing marginal return when the N is really big
    is_prime = [True] * (n + 1) 
    is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1): 
        if is_prime[i]: 
            for j in range(i*i, n + 1, i): # this will iterate through the list of numbers and determine if they are prime or not
                is_prime[j] = False 
    return is_prime, [x for x in range(2, n + 1) if is_prime[x]] # this will return the list of prime numbers
def is_prime_trial(n, small_primes=None): # this is a hybrid approach to see if its prime, using the sieve and trial division
    if n < 2:
        return False # failsafe for 0 and 1
    if n < 4:
        return True # numbers from 0 - 3 are always prime 
    if n % 2 == 0 or n % 3 == 0: # divisibility by 2 and 3
        return (n == 2 or n == 3)
    limit = int(math.isqrt(n)) # square root of n to limit the amount of numbers to check
    if small_primes:
        for p in small_primes: # is sieve is used, then it will check the prime numbers
            if p > limit: 
                break
            if n % p == 0: # if the number is divisible by the prime number, then it is not prime
                return (n == p)  
    else: # if sieve is not used, then it will use trial division
        i = 5
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
    return True
def extract_primes(binary_str, N): # main function
    if not all(index in "01" for index in binary_str): # edge case : only 0 and 1 are allowed
        return "0: Invalid binary strings "
    if type(N) is not int: # edge case : N must be an integer
        return "0: Invalid N given "
    candidates = set() # no dupes allowed
    length = len(binary_str)
    prefix = [0] * (length + 1)
    for i in range(length): # this will convert the binary string to a decimal number
        prefix[i+1] = (prefix[i] << 1) + (binary_str[i] == '1')
    for start in range(length): # this will iterate through the binary string
        for end in range(start + 1, length + 1): # this will iterate through the binary string
            val = prefix[end] - (prefix[start] << (end - start)) 
            if val >= N:
                break
            if val > 1:
                candidates.add(val) # this will add the number to the set
    if not candidates:
        return []
    max_candidate = max(candidates) # this will get the max number from the set
    SIEVE_THRESHOLD = 2_000_000  # this constant value is not so high on the curve but is good enought to produce the speed needed
    primes_found = []
    if max_candidate <= SIEVE_THRESHOLD: # if the max number is less than the threshold, then it will use the sieve
        is_prime_small, _ = sieve_upto(max_candidate) # this will get the prime numbers
        for val in sorted(candidates):
            if is_prime_small[val]: # if the number is prime, then it will add it to the list
                primes_found.append(val)
    else: # if the number is greater than the threshold, then it will use the hybrid approach
        is_prime_small, small_primes = sieve_upto(SIEVE_THRESHOLD) 
        for val in sorted(candidates):
            if val <= SIEVE_THRESHOLD:
                if is_prime_small[val]:
                    primes_found.append(val)
            else:
                if is_prime_trial(val, small_primes):
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
   print(extract_primes(input("Enter binary string: "), input("Enter N: ")))

# Code made and maintained by Elias Andrew Ailenei (github.com/eliasailenei) 