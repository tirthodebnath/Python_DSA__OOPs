##Bucket sort function-------------------------------

import math

## Insertion sort................

def insertion_sort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j=i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

#................................................................

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

cList = [1,5,6,2,4,8,965,962]
print(bucketSort(cList))

#----------------------------------------------------------