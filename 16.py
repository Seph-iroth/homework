#Lun Jiahao 2020.4.13
#show the runtime efficiency of different sorting method and operations
#there are read, serach, insert, and three sorting method, which is
#bubble, insertion, selection and mergesort
#count their run time 10 times and take the average speed
#Put all the time in to a table to compare
#with a graph show clearly the differece between the sorting method and operations.
import time
from random import randint
import matplotlib.pyplot as plt


def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count+= 1
    return count
def generateUnstoredArray(num): #how many element you want
    list = []
    for i in range(num):
        list.append(randint(0, 100))
    return list
def serach10(list):
    index = []
    count = 0
    for i in list:
        if i == 10:
            index.append(count)
        count += 1
    if len(index) == 0:
        return -1
    return index
#insert the element at the first place
def insertw(num, list):
    list.insert(0, num)
    return list
def findMiddle(list):
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)], list[int(len(list)/2+1)])

    else:
        return list[int(len(list)/2)]
#delele the second element
def dele2(list):
   list.pop(1)
   return list
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def insertionSort(array):
    for i in range(1,len(array)):
        pos = i
        temp = array[i]
        while (pos > 0) & (array[pos-1] > temp):
            array[pos] = array[pos -1]
            pos = pos - 1
        array[pos] = temp
    return array
def seletionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
        return array
def outputExample(array):
    print("Unsorted Array: ", array)
    print("Middle: ", findMiddle(array))
    print("Serach for 10: ", serach10(array))
    print("Insert 230 1st : ", insertw(230, array))
    print("Deletes second: ", dele2(array))
    print("Sorted n^2: ", bubblesort(array))
    print("Sorted < n^2: ", mergeSort(array))
    print("insertionSort: ", insertionSort(array))
    print("seletionSort: ", seletionSort(array))

#time the runtime 10 times and take the average
def timing(array):
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    y5 = 0
    y6 = 0
    y7 = 0
    y8 = 0
    for i in range(10):
        start = time.time()
        findMiddle(array)
        end = time.time()
        y1 = end - start + y1

        start = time.time()
        serach10(array)
        end = time.time()
        y2 = end - start + y2

        start = time.time()
        insertw(230, array)
        end = time.time()
        y3 = end - start + y3

        start = time.time()
        dele2(array)
        end = time.time()
        y4 = end - start + y4

        start = time.time()
        bubblesort(array)
        end = time.time()
        y5 = end - start + y5

        start = time.time()
        mergeSort(array)
        end = time.time()
        y6 = end - start + y6

        start = time.time()
        insertionSort(array)
        end = time.time()
        y7 = end - start + y7

        start = time.time()
        seletionSort(array)
        end = time.time()
        y8 = end - start + y8
    return [y1/10,y2/10,y3/10,y4/10,y5/10,y6/10,y7/10,y8/10]
#return the a row of one array timing
def finaltimetable(arraysize):
    print('    n       read          search        Insert        Delete        bubble sort   <n^2 sort     insertionSort seletionSort')
    timeOfEachArraySize = []
    for i in arraysize:
        array = generateUnstoredArray(i)
        timelist = timing(array)
        timeOfEachArraySize.append(timelist)
        print((countDigit(arraysize[-1])-countDigit(i))*" ",i, end='       ')
        for i in timelist:
            print("{:.2e}".format(i), end="      ")

        print("\n")
    return timeOfEachArraySize
def ploting(times, arraysize):
    ccount = 0
    for i in range(len(times[1])):
        runtime = []
        for i in range(len(arraysize)):
            runtime.append(times[i][ccount])
        plt.plot(arraysize, runtime)
        ccount += 1
    plt.xlabel('Array size')
    plt.ylabel('Time (seconds)')
    plt.title('')
    plt.show()

def main():
    arrays = generateUnstoredArray(5)
    outputExample(arrays)
    arraysize = [1,10,20,40,80,160,500,1000,2000,3000,4000,6000,10000]
    times = finaltimetable(arraysize)
    ploting(times,arraysize)
main()