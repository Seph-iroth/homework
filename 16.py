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
def generateUnstoredArray(num): # generate a num of size random Unstored array
    list = []
    for i in range(num):
        list.append(randint(0, 100))
    return list
def serach10(list): # search for 10 in the array
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
def bubblesort(array): #O(n^2)
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def insertionSort(array): #O    (n^2)
    for i in range(1,len(array)):
        pos = i
        temp = array[i]
        while (pos > 0) & (array[pos-1] > temp):
            array[pos] = array[pos -1]
            pos = pos - 1
        array[pos] = temp
    return array
def seletionSort(array):#   O(n^2)
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
def mergeSort(array):#  O(n log(n)
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
def timing(arraysize):
    timearray = [0,0,0,0,0,0,0,0]
    for i in range(10):
        array = generateUnstoredArray(arraysize)
        #generate samesize random array 10 times
        start = time.time()
        findMiddle(array)
        end = time.time()
        timearray[0] = end - start + timearray[0]

        start = time.time()
        serach10(array)
        end = time.time()
        timearray[1] = end - start + timearray[1]

        start = time.time()
        insertw(230, array)
        end = time.time()
        timearray[2] = end - start + timearray[2]

        start = time.time()
        dele2(array)
        end = time.time()
        timearray[3] = end - start + timearray[3]

        start = time.time()
        bubblesort(array)
        end = time.time()
        timearray[4] = end - start + timearray[4]

        start = time.time()
        mergeSort(array)
        end = time.time()
        timearray[5] = end - start + timearray[5]

        start = time.time()
        insertionSort(array)
        end = time.time()
        timearray[6] = end - start + timearray[6]

        start = time.time()
        seletionSort(array)
        end = time.time()
        timearray[7] = end - start + timearray[7]
    output =[]
    for i in timearray:
        output.append(i/10) #/10 to get the average
    return output#return the a row of one array timing
def finaltimetable(arraysize): # arange the table
    print('    n       read          search        Insert        Delete        bubble sort   <n^2 sort     insertionSort seletionSort')
    timeOfEachArraySize = []
    for i in arraysize:
        timelist = timing(i)
        timeOfEachArraySize.append(timelist)
        print((countDigit(arraysize[-1])-countDigit(i))*" ",i, end='       ')
        for i in timelist:
            print("{:.2e}".format(i), end="      ")
        print("\n")
    return timeOfEachArraySize
def ploting(times, arraysize): #plot the time verse zrray size
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
    start = time.time()
    arrays = generateUnstoredArray(5)
    outputExample(arrays)
    arraysize = [1,10,20,40,80,160,500,1000,3000]#,4500,6000,10000,20000,50000]
    times = finaltimetable(arraysize)
    end = time.time()
    print("Total runtime: ", ((round((end - start)/60, 4))), " min")
    ploting(times, arraysize)

main()
