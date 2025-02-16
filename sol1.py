def check(binary):
    return all(index in "01" for index in binary)
def hidden(binary):
    data = set()
    length = len(binary)
    if check(binary):
        prefix = [0] * (length + 1)  
        for i in range(length):
            prefix[i + 1] = (prefix[i] << 1) + int(binary[i])
        for i in range(length):
            for j in range(i + 1, length + 1):
                val = prefix[j] - (prefix[i] << (j - i))
                if val > 1:  
                    data.add(val)
    return sorted(data)  
def is_prime(n):
    if n < 2:
        return False
    if n in {2, 3, 5, 7, 11}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def sort(array, less):
    array = [num for num in array if num <= less and is_prime(num)]
    array = sorted(set(array))  
    if len(array) == 0:
        return "No primes found."
    if len(array) > 6:
        return f"{array[0]} {array[1]} {array[2]} {array[-3]} {array[-2]} {array[-1]} : {len(array)}"
    return " ".join(map(str, array))
def final(array, less):
    print(sort(array, less))
def work(array, less):
    values = hidden(array)
    final(values, less)
test_binary = "01000011010011110100110101010000001100010011100000110001"
test_limit = 123456789012
work(test_binary, test_limit)
