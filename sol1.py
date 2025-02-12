def check(binary):
    approve = True
    for index in binary:
        if index != "1":
            if index != "0":
                approve = False
    return approve


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
                string = string + binary[x]
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


def sort(array, less):
    array = prime(array)
    swap = True
    while swap:
        swap = False
        if array[0] == -1:
            array.remove(-1)
            swap = True
        if array[-1] > less:
            array[-1] = -1
            swap = True

        for element in range(len(array)):
            for index in range(len(array) - 1):
                if array[index] > array[index + 1]:
                    temp = array[index]
                    array[index] = array[index + 1]
                    array[index + 1] = temp
                    swap = True
    return array


def final(array, less):
    array = sort(array, less)
    if len(array) > 6:
        print(array[0], array[1], array[2], array[-3], array[-2], array[-1], ":", len(array))
    else:
        print(array)


def work(array, less):
    values = hidden(array)
    datas = []
    for element1 in values:
        total = 0
        for element2 in convert(element1):
            total += element2
        datas.append(total)
    final(datas, less)


work("011011", 10)
