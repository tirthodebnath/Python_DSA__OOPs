## How to find maximum product of two number from list

numarry = [1,2,3,4,5,6,7,8,9,0,1,23,4,22]

def arr1(array):
    target=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] * array[j] > target:
                target = array[i] * array[j]
                pairs = str(array[i]) +","+str(array[j])
    print(pairs)
    print(target)
arr1(numarry)    
    

