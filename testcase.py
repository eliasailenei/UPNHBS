import unittest
import time
import math
import functools

#################################
# sol2 module code starts here: # AI GENERATED CODE
#################################

import sympy  # will be removed from final submission (as your comment suggests)

def sieve(limit):  # this method has a limit btw
    is_prime_arr = bytearray(b'\x01') * (limit + 1) 
    is_prime_arr[:2] = b'\x00\x00'  # 0 and 1 are not prime
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime_arr[i]:  # if it's prime
            # Mark multiples of i as not prime
            is_prime_arr[i * i : limit + 1 : i] = b'\x00' * ((limit - i * i) // i + 1)
    return [i for i, prime in enumerate(is_prime_arr) if prime]

SMALL_PRIMES_LIST = sieve(10_000_000)  # generate a list of small primes
SMALL_PRIMES = set(SMALL_PRIMES_LIST)

@functools.lru_cache(maxsize=None)
def is_prime(n):  # trial division method
    if n < 2:
        return False
    if n in SMALL_PRIMES:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = math.isqrt(n)
    for p in SMALL_PRIMES_LIST:
        if p > r:
            return True
        if n % p == 0:
            return False
    i = 5
    while i <= r:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
        last_three = [f"{n} --> {'✅' if sympy.isprime(n) else '❌'}" for n in primes[-3:]]
        return f"6: {', '.join(map(str, primes[:3]))}, ..., {', '.join(last_three)}"


######################################
#   1. TestSieveFunction             #
######################################

class TestSieveFunction(unittest.TestCase):

    def test_small_sieve(self):
        """Check sieve with a very small limit."""
        self.assertEqual(sieve(1), [], "Sieve up to 1 should return [].")
        self.assertEqual(sieve(2), [2], "Sieve up to 2 should return [2].")

    def test_medium_sieve(self):
        """Check sieve with a medium limit."""
        result = sieve(30)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(result, expected, "Sieve up to 30 should match known primes.")

    def test_larger_sieve(self):
        """Check sieve with a larger limit."""
        result = sieve(100)
        self.assertIn(97, result, "97 should appear in sieve(100).")
        self.assertNotIn(99, result, "99 should not appear in sieve(100).")


######################################
#   2. TestIsPrimeFunction           #
######################################

class TestIsPrimeFunction(unittest.TestCase):

    def test_negative_number(self):
        """Negative numbers are never prime."""
        self.assertFalse(is_prime(-5), "Negative numbers must return False.")

    def test_zero_not_prime(self):
        """0 is not prime."""
        self.assertFalse(is_prime(0), "Zero must return False.")

    def test_one_not_prime(self):
        """1 is not prime."""
        self.assertFalse(is_prime(1), "One must return False.")

    def test_two_is_prime(self):
        """2 is the smallest (and only even) prime."""
        self.assertTrue(is_prime(2), "2 should be prime.")

    def test_small_prime(self):
        """7 is prime."""
        self.assertTrue(is_prime(7), "7 should be prime.")

    def test_small_composite(self):
        """9 is not prime."""
        self.assertFalse(is_prime(9), "9 should not be prime.")

    def test_even_composite(self):
        """Check a typical even composite number."""
        self.assertFalse(is_prime(100), "100 is composite (10*10).")

    def test_larger_prime(self):
        """Check a larger known prime, e.g., 7919."""
        self.assertTrue(is_prime(7919), "7919 is a known prime.")

    def test_larger_composite(self):
        """Check a large composite number, e.g. 7920 = 80*99."""
        self.assertFalse(is_prime(7920), "7920 is not prime.")


######################################
#   3. TestGetCandidatesFunction     #
######################################

class TestGetCandidatesFunction(unittest.TestCase):

    def test_simple_binary_1(self):
        """
        For '1011' (decimal 11) with N=16:
          - Substrings can yield 1,0,1,1,2,3,5,11, etc.
          - Exclude values >=16 or <=1
          - We expect {2,3,5,11}.
        """
        binary_str = '1011'
        N = 16
        candidates = get_candidates(binary_str, N)
        self.assertEqual(candidates, {2, 3, 5, 11})

    def test_simple_binary_2(self):
        """
        '111' with N=8 => possible substrings >1,<8 => {3,7}.
        """
        binary_str = '111'
        N = 8
        candidates = get_candidates(binary_str, N)
        self.assertEqual(candidates, {3, 7})

    def test_all_zeroes(self):
        """'0000' -> no substring above 1, so empty."""
        binary_str = '0000'
        N = 8
        candidates = get_candidates(binary_str, N)
        self.assertEqual(candidates, set(), "All zeroes yield no numbers >1.")


##############################################
# 4. Performance test (fails if > 60 seconds) #
##############################################

class TestExtractPrimesPerformance(unittest.TestCase):

    def test_custom_cases(self):
        """
        Loop through multiple (binary_str, N) test cases.
        Fail if any single test case exceeds 60 seconds.
        """
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

        for idx, (binary_str, n) in enumerate(test_cases):
            with self.subTest(case=idx + 1):
                start_time = time.time()

                # Call the function under test
                result = extract_primes(binary_str, n)

                elapsed_time = time.time() - start_time
                print(f"[Performance] Test case {idx+1} took {elapsed_time:.6f} seconds.")

                # Fail if the test took more than 60 seconds
                self.assertLess(
                    elapsed_time,
                    60,
                    f"Test case {idx+1} exceeded 60 seconds!"
                )

                self.assertIsInstance(result, str)


###########################
# Entry point for testing #
###########################

if __name__ == '__main__':
    unittest.main(verbosity=2)
