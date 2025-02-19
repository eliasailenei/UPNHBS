import unittest
import sol1, sol2
import time
import math
import random
import functools
import matplotlib.pyplot as plt

class TestExtractPrimesPerformance(unittest.TestCase):
    
    execution_times = []  # Store execution times
    test_case_indices = list(range(1, 12))  # Test case numbers

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
                result = sol1.extract_primes(binary_str, n)

                elapsed_time = time.time() - start_time
                self.execution_times.append(elapsed_time)  # Store execution time

                print(f"[Performance] Test case {idx+1} took {elapsed_time:.6f} seconds.")

                # Fail if the test took more than 60 seconds
                self.assertLess(
                    elapsed_time,
                    60,
                    f"Test case {idx+1} exceeded 60 seconds!"
                )

                self.assertIsInstance(result, str)

    @classmethod
    def tearDownClass(cls):
        """ Generate a graph after tests complete """
        plt.figure(figsize=(10, 5))
        plt.plot(cls.test_case_indices[:len(cls.execution_times)], cls.execution_times, marker='o', linestyle='-', label="Execution Time (s)")

        # Labels and title
        plt.xlabel("Test Case Number")
        plt.ylabel("Execution Time (s)")
        plt.title("Performance of extract_primes Function Across Test Cases")
        plt.xticks(cls.test_case_indices[:len(cls.execution_times)])
        plt.grid(True)
        plt.legend()

        # Show the plot
        plt.show()


###########################
# Entry point for testing #
###########################

if __name__ == '__main__':
    unittest.main(verbosity=2)
