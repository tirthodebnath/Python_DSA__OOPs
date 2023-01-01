## Insertion sort

def insertion_sort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j=i-1
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList)

clist=[1,2,4,2,4,1]
insertion_sort(clist)