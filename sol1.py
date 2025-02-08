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


def hidden(value):
    increment = 0
    data = []
    while increment != len(value):
        string = ""
        for x in range((len(value)) - increment):
            string = string + value[x]
        data.append(string)
        increment += 1
    return data


values = hidden(value)
datas = []
for element1 in values:
    sum = 0
    for element2 in convert(element1):
        sum += element2
    datas.append(sum)

datas.append(2)
