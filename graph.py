import time
import matplotlib.pyplot as plt
import sol2  # Assuming sol2 is provided
import sol1  # Assuming sol1 is provided
import sol3  # Assuming sol3 is provided and similar to sol2

def run_case(binary_str, n, solution, header):
    start_time = time.perf_counter_ns()  
    output_sol = solution.extract_primes(binary_str, n)
    elapsed_time_ns = time.perf_counter_ns() - start_time  

    if elapsed_time_ns < 1_000:  # Less than 1µs
        formatted_time = f"{elapsed_time_ns} ns"
    elif elapsed_time_ns < 1_000_000:  # Less than 1ms
        formatted_time = f"{elapsed_time_ns / 1_000:.3f} µs"
    elif elapsed_time_ns < 1_000_000_000:  # Less than 1s
        formatted_time = f"{elapsed_time_ns / 1_000_000:.3f} ms"
    else:
        formatted_time = f"{elapsed_time_ns / 1_000_000_000:.6f} s"

    elapsed_time_s = elapsed_time_ns / 1_000_000_000  # Convert to seconds
    return f" {header}: \n  Time taken: {formatted_time} \n  Answer: {output_sol}", elapsed_time_s

# Define test cases
test_cases = [
    ("0100001101001111", 999999),
    ("01000011010011110100110101010000", 999999),
    ("1111111111111111111111111111111111111111", 999999),
    ("010000110100111101001101010100000011000100111000", 999999999),
    ("01000011010011110100110101010000001100010011100000110001", 123456789012),
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678),
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789),
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789),
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890),
]

# Store execution times
execution_times_sol1 = []
execution_times_sol2 = []
execution_times_sol3 = []
test_case_indices = list(range(1, len(test_cases) + 1))

# Run performance tests
for idx, (binary_str, n) in enumerate(test_cases):
    print(f"Test Case {idx + 1}")
    
    result, time_sol1 = run_case(binary_str, n, sol1, "Solution 1")
    execution_times_sol1.append(time_sol1)
    print(result)

    result, time_sol2 = run_case(binary_str, n, sol2, "Solution 2")
    execution_times_sol2.append(time_sol2)
    print(result)

    result, time_sol3 = run_case(binary_str, n, sol3, "Solution 2 - holy trinity")
    execution_times_sol3.append(time_sol3)
    print(result)

# Plot execution times
plt.figure(figsize=(10, 5))
plt.plot(test_case_indices, execution_times_sol1, marker='o', linestyle='-', label="Solution 1")
plt.plot(test_case_indices, execution_times_sol2, marker='s', linestyle='--', label="Solution 2")
plt.plot(test_case_indices, execution_times_sol3, marker='d', linestyle='-.', label="Solution 2 - the holy trinity")

plt.xlabel("Test Case Number")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time Comparison: Solution 1, 2, and 3")
plt.xticks(test_case_indices)
plt.grid(True)
plt.legend()
plt.show()

# Plot execution times for only Solution 2 - holy trinity
plt.figure(figsize=(10, 5))
plt.plot(test_case_indices, execution_times_sol3, marker='d', linestyle='-.', color='r', label="Solution 2 - the holy trinity")

plt.xlabel("Test Case Number")
plt.ylabel("Execution Time (s)")
plt.title("Execution Time: Solution 2 - The Holy Trinity")
plt.xticks(test_case_indices)
plt.grid(True)
plt.legend()
plt.show()

