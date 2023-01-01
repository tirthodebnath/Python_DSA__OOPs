## Selection sort order

def selectionsort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    
    print(customList)

clist=[2,4,5,6,2,4]
selectionsort(clist)