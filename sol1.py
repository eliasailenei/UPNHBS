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
    elif len(array) < 6:
        return f"{len(array)}: {', '.join(map(str, array))}"
    else:
        last_three = [f"{n}" for n in array[-3:]]
        return f"6: {', '.join(map(str, array[:3]))}, ..., {', '.join(last_three)}"
def final(array, less):
    return (sort(array, less))
def extract_primes(array, less):
    values = hidden(array)
    return final(values, less)