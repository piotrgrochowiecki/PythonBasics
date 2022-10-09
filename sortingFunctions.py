def dataInput(values, size):
    for i in range(size):
        values.append(float(input("Please provide a number: ")))
    return

def sortData(values, size):

    for x in range(size):
        for ctr in range(size - 1):
            if (values[ctr] > values[ctr + 1]):
                temp = values[ctr]
                values[ctr] = values[ctr + 1]
                values[ctr + 1] = temp

def printData(values, size):
    for i in range(size):
        print(values[i])