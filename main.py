import sortingFunctions

numSize = int(input("Please specify array size: "))
numSet = []

sortingFunctions.dataInput(numSet, numSize)
print("Before sorting: ")
sortingFunctions.printData(numSet, numSize)

sortingFunctions.sortData(numSet, numSize)

print("After sorting: ")
sortingFunctions.printData(numSet, numSize)
