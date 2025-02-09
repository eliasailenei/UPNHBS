value = "0110"


def check(binary):
    work = True
    for index in binary:
        if index != "1":
            if index != "0":
                work = False
    return work


def convert(binary):
    data = []
    exponential = len(binary) - 1
    for x in range(len(binary)):
        data.append(2 ** exponential * int(binary[x]))
        exponential -= 1
    return data


def hidden(binary):
    increment = 0
    data = []
    if check(binary):
        while increment != len(binary):
            string = ""
            for x in range((len(binary)) - increment):
                string = string + value[x]
            data.append(string)
            increment += 1
        return data


def prime(array):
    primed = [2, 3, 5, 7, 11]
    for index in range(len(array)):
        for element in primed:
            if array[index] != element:
                if array[index] > 3:
                    if array[index] % element == 0:
                        array[index] = -1

                else:
                    if array[index] == 1 or array[index] == 0:
                        array[index] = -1

    return array





