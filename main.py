numbers = [12, 34, 40, 87, 99]

searchNumber = int(input("Provide searched number: "))

foundNumber = 0
first = 0
last = len(numbers) - 1

while (first <= last):
    mid = int((first + last)/2)
    if (searchNumber == numbers[mid]):
        print("Array contains number: ", searchNumber)
        foundNumber = 1
        break
    elif (searchNumber < numbers[mid]):
        last = mid - 1
    else:
        first = mid + 1

if (foundNumber == 0):
    print("Array does not contain number ", searchNumber)
