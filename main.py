numbers = [34, 87, 12, 99, 40]

searchNumber = int(input("Provide searched number: "))

foundNumber = 0

for i in range(len(numbers)):
    if (numbers[i] == searchNumber):
        print("Array contains number " + str(searchNumber))

        foundNumber = 1
        break

if (foundNumber == 0):
    print("Array does not contains number " + str(searchNumber))
