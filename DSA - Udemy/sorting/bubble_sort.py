## Bubble sort function

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-1):
            if customList[j]>customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    
    print(customList)

clist=[2,4,5,6,2,46]
bubbleSort(clist)