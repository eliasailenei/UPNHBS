import time
import matplotlib.pyplot as plt
import sol2  # Assuming sol2 is provided
import sol1  # Assuming sol1 is provided
import sol3  # Since sol3 is nearly identical to sol2, we alias it for clarity

# Test cases for performance evaluation
test_cases = [
    ("0100001101001111", 999999), # 1
    ("01000011010011110100110101010000", 999999), # 2
    ("1111111111111111111111111111111111111111", 999999), # 3
    ("010000110100111101001101010100000011000100111000", 999999999), # 4
    ("01000011010011110100110101010000001100010011100000110001", 123456789012), # 5
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345), # 6
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678), # 7
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789), # 8
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789), # 9
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890) # 10
]

# Store execution times and results for each solution
execution_times_sol1 = []
execution_times_sol2 = []
execution_times_sol3 = []
test_case_indices = list(range(1, len(test_cases) + 1))

# Run performance tests
for idx, (binary_str, n) in enumerate(test_cases):
    print(f"Test Case {idx + 1}")

    # # Solution 1
    # start_time = time.time()
    # output_sol1 = sol1.extract_primes(binary_str, n)
    # elapsed_time_sol1 = time.time() - start_time
    # execution_times_sol1.append(elapsed_time_sol1)
    # print(f"Solution 1:\n  Time taken: {elapsed_time_sol1:.6f}s\n  Answer: {output_sol1}")

    # Solution 2
    start_time = time.time()
    output_sol2 = sol2.extract_primes(binary_str, n)
    elapsed_time_sol2 = time.time() - start_time
    execution_times_sol2.append(elapsed_time_sol2)
    print(f"Solution 2 - new:\n  Time taken: {elapsed_time_sol2:.6f}s\n  Answer: {output_sol2}")

    # Solution 3
    start_time = time.time()
    output_sol3 = sol3.extract_primes(binary_str, n)
    elapsed_time_sol3 = time.time() - start_time
    execution_times_sol3.append(elapsed_time_sol3)
    print(f"Solution 2 - old:\n  Time taken: {elapsed_time_sol3:.6f}s\n  Answer: {output_sol3}\n")

# Plot execution times
plt.figure(figsize=(10, 5))
#plt.plot(test_case_indices, execution_times_sol1, marker='o', linestyle='-', label="Solution 1")
plt.plot(test_case_indices, execution_times_sol2, marker='s', linestyle='--', label="Solution 2 - new")
plt.plot(test_case_indices, execution_times_sol3, marker='d', linestyle='-.', label="Solution 2 - old")

# Labels and title
plt.xlabel("Test Case Number")
plt.ylabel("Execution Time (s)")
plt.title("Performance of extract_primes Function Across Test Cases")
plt.xticks(test_case_indices)
plt.grid(True)
plt.legend()

# Show the plot
plt.show() 