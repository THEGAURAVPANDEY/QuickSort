data = []

 #Partition function
    
def partition(array, start, end):

    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[end]) = (array[end], array[i + 1])

    return i + 1
 
# quicksort function 

def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)

        quickSort(array, start, pivot - 1)

        quickSort(array, pivot + 1, end)
        
        #input function

def inputArray():
    arrayResult = []

    totalNumbers = int(input('Total numbers to input. '))

    for i in range(totalNumbers):
        inputNumber = int(input('Enter the number: '))
        arrayResult.append(inputNumber)

    return arrayResult

 

result = int(input('Welcome.\n1.- Insert numbers manually\n2.-Insert numbers automatically (worst case scenario)\n'))

if(result == 1):
    data = inputArray()
elif (result == 2):
    for i in range(20, 0, -1):
        data.append(i)
        
# to print the unsorted array

print("TheUnsorted array:")
print(data)
 
  #length of the given array.

size = len(data)
 
quickSort(data, 0, size - 1)

# to print the sorted array
    
  
print('Sorted Array:')
print(data)
