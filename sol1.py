def check(binary):
    return all(index in "01" for index in binary) # this will check if the binary string is valid
def hidden(binary):
    data = set() # no dupes allowed
    length = len(binary)
    if check(binary): # if the binary string is valid, then it will convert it to a decimal number
        prefix = [0] * (length + 1)  
        for i in range(length):
            prefix[i + 1] = (prefix[i] << 1) + int(binary[i]) 
        for i in range(length):
            for j in range(i + 1, length + 1):
                val = prefix[j] - (prefix[i] << (j - i))
                if val > 1:  
                    data.add(val)
    return sorted(data)  
def is_prime(n): # only using trial division here, very simple and fast
    if n < 2: # even numbers are not prime
        return False
    if n in {2, 3, 5, 7, 11}: # these are the only prime numbers that are not divisible by 2 or 3
        return True
    if n % 2 == 0 or n % 3 == 0: # if the number is divisible by 2 or 3, then it is not prime
        return False
    i = 5
    while i * i <= n: # this will iterate through the number and check if it is prime
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def sort(array, less): # this will sort the array and check if the number is prime
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
    if not all(index in "01" for index in array):
        return "0: Invalid binary strings "
    if type(less) is not int:
        return "0: Invalid N given "
    values = hidden(array)
    return final(values, less)

if __name__ == "__main__":
    print(extract_primes(input("Enter a binary string: "), int(input("Enter N: "))))

# Code made by Lloyd and Caleb. Reviewed and commented by Elias Andrew Ailenei (github.com/eliasailenei)